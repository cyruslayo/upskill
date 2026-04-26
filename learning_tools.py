"""Colab-first learning helpers for the interactive math curriculum.

The functions in this module are intentionally lightweight: they work in a
plain notebook, in Google Colab, and in local Jupyter without requiring a
backend service.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta, timezone
import json
import math
import os
import re
from pathlib import Path
from typing import Any, Callable, Iterable


SCHEMA_VERSION = 1
DEFAULT_PROGRESS_FILENAME = "upskill_math_progress.json"
DRIVE_PROGRESS_DIR = "MyDrive/upskill"


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def _parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


@dataclass
class Skill:
    """A small curriculum skill descriptor."""

    id: str
    title: str
    notebook: str
    level: int
    prerequisites: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def setup_colab(
    progress_filename: str = DEFAULT_PROGRESS_FILENAME,
    mount_drive: bool = True,
    verbose: bool = True,
) -> Path:
    """Prepare a notebook session and return the progress-file path.

    In Colab, this mounts Google Drive when available. Outside Colab, it falls
    back to the current working directory.
    """

    progress_path = Path(progress_filename)
    try:
        import google.colab  # type: ignore  # noqa: F401
        in_colab = True
    except Exception:
        in_colab = False

    if in_colab and mount_drive:
        try:
            from google.colab import drive  # type: ignore

            drive.mount("/content/drive")
            drive_dir = Path("/content/drive") / DRIVE_PROGRESS_DIR
            drive_dir.mkdir(parents=True, exist_ok=True)
            progress_path = drive_dir / progress_filename
        except Exception as exc:
            if verbose:
                print(f"Drive mount skipped; using local progress file. ({exc})")

    if verbose:
        print(f"Learning environment ready. Progress: {progress_path}")
    return progress_path


class ProgressStore:
    """JSON-backed spaced-repetition progress store."""

    def __init__(self, path: str | Path | None = None, learner_id: str = "local"):
        self.path = Path(path or DEFAULT_PROGRESS_FILENAME)
        self.learner_id = learner_id
        self.data = self._load()

    def _default_data(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "learner_id": self.learner_id,
            "skills": {},
        }

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return self._default_data()
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except Exception:
            return self._default_data()
        if data.get("schema_version") != SCHEMA_VERSION:
            data["schema_version"] = SCHEMA_VERSION
        data.setdefault("learner_id", self.learner_id)
        data.setdefault("skills", {})
        return data

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")

    def get(self, skill_id: str) -> dict[str, Any]:
        return self.data.setdefault("skills", {}).setdefault(skill_id, {
            "attempts": 0,
            "correct": 0,
            "confidence": 0,
            "mastery": 0.0,
            "last_seen": None,
            "next_review": None,
        })

    def record_attempt(
        self,
        skill_id: str,
        correct: bool,
        confidence: int = 3,
        item_type: str = "practice",
    ) -> dict[str, Any]:
        confidence = max(1, min(5, int(confidence)))
        row = self.get(skill_id)
        attempts = int(row.get("attempts", 0)) + 1
        correct_count = int(row.get("correct", 0)) + int(bool(correct))
        accuracy = correct_count / attempts
        confidence_factor = confidence / 5
        mastery = round((0.75 * accuracy) + (0.25 * confidence_factor), 3)

        row.update({
            "attempts": attempts,
            "correct": correct_count,
            "confidence": confidence,
            "mastery": mastery,
            "last_seen": _iso(_utcnow()),
            "last_item_type": item_type,
            "next_review": _iso(_utcnow() + review_interval(correct, confidence, attempts)),
        })
        self.save()
        return row

    def review_queue(
        self,
        skills: Iterable[Skill | dict[str, Any]] | None = None,
        limit: int = 8,
        now: datetime | None = None,
    ) -> list[dict[str, Any]]:
        now = now or _utcnow()
        known_titles = {}
        if skills:
            for skill in skills:
                item = skill.to_dict() if isinstance(skill, Skill) else skill
                known_titles[item["id"]] = item

        due: list[dict[str, Any]] = []
        for skill_id, row in self.data.get("skills", {}).items():
            next_review = _parse_iso(row.get("next_review"))
            if next_review is None or next_review <= now:
                due.append({
                    "id": skill_id,
                    "title": known_titles.get(skill_id, {}).get("title", skill_id),
                    "mastery": row.get("mastery", 0.0),
                    "next_review": row.get("next_review"),
                    "attempts": row.get("attempts", 0),
                })
        due.sort(key=lambda item: (item["mastery"], item["next_review"] or ""))
        return due[:limit]

    def weak_skills(self, limit: int = 8) -> list[tuple[str, dict[str, Any]]]:
        rows = list(self.data.get("skills", {}).items())
        rows.sort(key=lambda kv: (kv[1].get("mastery", 0.0), -kv[1].get("attempts", 0)))
        return rows[:limit]


def review_interval(correct: bool, confidence: int, attempts: int = 1) -> timedelta:
    """Return the next review interval from correctness and confidence."""

    if not correct:
        return timedelta(hours=6) if attempts <= 1 else timedelta(days=1)
    if confidence <= 2:
        return timedelta(days=1)
    if confidence == 3:
        return timedelta(days=3)
    high_confidence_days = [7, 14, 30, 60]
    return timedelta(days=high_confidence_days[min(max(attempts - 1, 0), len(high_confidence_days) - 1)])


def record_attempt(
    skill_id: str,
    correct: bool,
    confidence: int = 3,
    item_type: str = "practice",
    store: ProgressStore | None = None,
) -> dict[str, Any]:
    store = store or ProgressStore()
    return store.record_attempt(skill_id, correct, confidence, item_type)


def review_queue(
    skills: Iterable[Skill | dict[str, Any]] | None = None,
    limit: int = 8,
    store: ProgressStore | None = None,
) -> list[dict[str, Any]]:
    store = store or ProgressStore()
    return store.review_queue(skills=skills, limit=limit)


def check(
    name: str,
    actual: Any,
    expected: Any,
    tolerance: float | None = None,
    skill_id: str | None = None,
    confidence: int = 3,
    store: ProgressStore | None = None,
) -> bool:
    """Friendly equality/numeric check with optional progress recording."""

    if tolerance is not None and isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
        ok = math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance)
    else:
        ok = actual == expected

    if ok:
        print(f"PASS: {name}")
    else:
        print(f"TRY AGAIN: {name}")
        print(f"  expected: {expected!r}")
        print(f"  actual:   {actual!r}")

    if skill_id:
        record_attempt(skill_id, ok, confidence, "check", store)
    return ok


def code_check(
    name: str,
    fn: Callable[..., Any],
    cases: Iterable[tuple[tuple[Any, ...], Any] | tuple[tuple[Any, ...], dict[str, Any], Any]],
    skill_id: str | None = None,
    confidence: int = 3,
    store: ProgressStore | None = None,
) -> bool:
    """Run multiple function cases and report the first failure."""

    all_ok = True
    for index, case in enumerate(cases, 1):
        if len(case) == 2:
            args, expected = case  # type: ignore[misc]
            kwargs = {}
        else:
            args, kwargs, expected = case  # type: ignore[misc]
        try:
            actual = fn(*args, **kwargs)
            ok = actual == expected
        except Exception as exc:
            actual = f"{type(exc).__name__}: {exc}"
            ok = False
        if not ok:
            all_ok = False
            print(f"TRY AGAIN: {name} case {index}")
            print(f"  args:     {args}")
            print(f"  expected: {expected!r}")
            print(f"  actual:   {actual!r}")
            break
    if all_ok:
        print(f"PASS: {name} ({index} cases)")
    if skill_id:
        record_attempt(skill_id, all_ok, confidence, "code_check", store)
    return all_ok


def normalize_answer(value: Any) -> str:
    text = str(value).strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9.+/=\- ]", "", text)
    text = re.sub(r"\s*=\s*", "=", text)
    return text


def short_answer_check(
    name: str,
    answer: Any,
    accepted: Iterable[Any],
    skill_id: str | None = None,
    confidence: int = 3,
    store: ProgressStore | None = None,
) -> bool:
    normalized = normalize_answer(answer)
    accepted_norm = {normalize_answer(item) for item in accepted}
    ok = normalized in accepted_norm
    print(f"{'PASS' if ok else 'TRY AGAIN'}: {name}")
    if not ok:
        print("  Re-read the prompt and try to retrieve the answer before opening a hint.")
    if skill_id:
        record_attempt(skill_id, ok, confidence, "short_answer", store)
    return ok


def hint_box(title: str, hints: list[str], unlock: bool = False) -> None:
    """Display staged hints. Full hints require unlock=True."""

    print(title)
    if not hints:
        print("No hints for this item.")
        return
    if not unlock:
        print(f"Hint 1: {hints[0]}")
        print("Run again with unlock=True after a real attempt to see more.")
        return
    for index, hint in enumerate(hints, 1):
        print(f"Hint {index}: {hint}")


def render_quiz(quiz_data: list[dict[str, Any]]) -> None:
    """Render a JupyterQuiz when available, otherwise print a plain fallback."""

    try:
        from jupyterquiz import display_quiz  # type: ignore

        display_quiz(quiz_data)
        return
    except Exception:
        pass

    print("Quiz fallback")
    print("=============")
    for index, item in enumerate(quiz_data, 1):
        prompt = item.get("question") or item.get("prompt") or f"Question {index}"
        print(f"{index}. {prompt}")
        for choice in item.get("choices", []):
            if isinstance(choice, dict):
                print(f"   - {choice.get('answer', choice)}")
            else:
                print(f"   - {choice}")


def mastery_dashboard(
    store: ProgressStore | None = None,
    skills: Iterable[Skill | dict[str, Any]] | None = None,
    next_notebook: str | None = None,
) -> None:
    store = store or ProgressStore()
    due = store.review_queue(skills=skills)
    weak = store.weak_skills()
    total = len(store.data.get("skills", {}))
    mastered = sum(1 for row in store.data.get("skills", {}).values() if row.get("mastery", 0) >= 0.8)

    print("Mastery Dashboard")
    print("=================")
    print(f"Skills attempted: {total}")
    print(f"Skills at mastery >= 0.80: {mastered}")
    if due:
        print("\nDue for review:")
        for item in due:
            print(f"- {item['title']} (mastery {item['mastery']})")
    else:
        print("\nNo due reviews yet.")
    if weak:
        print("\nWeakest skills:")
        for skill_id, row in weak:
            print(f"- {skill_id}: mastery {row.get('mastery', 0)} after {row.get('attempts', 0)} attempts")
    if next_notebook:
        print(f"\nRecommended next notebook: {next_notebook}")
