"""Shared implementations for migrated legacy instructor solution notebooks."""
from __future__ import annotations

from collections import Counter, deque
import heapq
import itertools
import math
import random
from typing import Any

import numpy as np


ALPHABET = " abcdefghijklmnopqrstuvwxyz"


def check_if_symmetric(string: str) -> bool:
    cleaned = string.lower()
    return cleaned == cleaned[::-1]


def count_characters(string: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in string.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n))
    for factor in range(3, limit + 1, 2):
        if n % factor == 0:
            return False
    return True


def symmetric_prime_counts(string: str) -> dict[str, Any]:
    counts = count_characters(string)
    return {
        "is_symmetric": check_if_symmetric(string),
        "character_counts": counts,
        "prime_count_letters": {ch: is_prime(count) for ch, count in counts.items()},
    }


def binary_to_decimal(string: str) -> int:
    total = 0
    for bit in string:
        total = total * 2 + int(bit)
    return total


def decimal_to_hexadecimal(string: str | int) -> str:
    digits = "0123456789ABCDEF"
    n = int(string)
    if n == 0:
        return "0"
    sign = "-" if n < 0 else ""
    n = abs(n)
    out = []
    while n > 0:
        out.append(digits[n % 16])
        n //= 16
    return sign + "".join(reversed(out))


def binary_to_hexadecimal(string: str) -> str:
    return decimal_to_hexadecimal(binary_to_decimal(string))


def is_binary_symmetric(decimal_string: str) -> bool:
    return check_if_symmetric(bin(int(decimal_string))[2:])


def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def collatz_sequence(n: int) -> list[int]:
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def count_prime_collatz(n: int) -> int:
    return sum(1 for value in collatz_sequence(n) if is_prime(value))


def flip_coin() -> int:
    return random.randint(0, 1)


def sim_probability(num_trials: int, event_fn) -> float:
    successes = 0
    for _ in range(num_trials):
        successes += int(bool(event_fn()))
    return successes / num_trials if num_trials else 0.0


def average_binary_flips(num_trials: int, target_flips: int = 10) -> float:
    total = 0
    for _ in range(num_trials):
        total += sum(flip_coin() for _ in range(target_flips))
    return total / num_trials if num_trials else 0.0


def get_cumulative_distribution(probabilities: list[float]) -> list[float]:
    total = 0.0
    out = []
    for p in probabilities:
        total += p
        out.append(total)
    return out


def sample_index(probabilities: list[float]) -> int:
    cdf = get_cumulative_distribution(probabilities)
    r = random.random()
    for i, cutoff in enumerate(cdf):
        if r <= cutoff:
            return i
    return len(probabilities) - 1


def verify_distribution(probabilities: list[float], trials: int = 5000) -> list[float]:
    counts = [0] * len(probabilities)
    for _ in range(trials):
        counts[sample_index(probabilities)] += 1
    return [count / trials for count in counts]


def cartesian_product_2d(array1: list[Any], array2: list[Any]) -> list[list[Any]]:
    return [[a, b] for a in array1 for b in array2]


def calc_cartesian_product(arrays: list[list[Any]]) -> list[list[Any]]:
    product = [[]]
    for array in arrays:
        product = [prefix + [item] for prefix in product for item in array]
    return product


def sample_from_cartesian(arrays: list[list[Any]]) -> list[Any]:
    return [random.choice(array) for array in arrays]


def algebraic_inverse(fx: int, a: int, b: int) -> float:
    return (fx - b) / a


def encode_string(string: str, a: int, b: int) -> list[int]:
    out = []
    for ch in string.lower():
        idx = ALPHABET.index(ch) if ch in ALPHABET else 0
        out.append(a * idx + b)
    return out


def decode_numbers(numbers: list[int], a: int, b: int) -> str:
    chars = []
    for number in numbers:
        idx = int(algebraic_inverse(number, a, b))
        idx = max(0, min(idx, len(ALPHABET) - 1))
        chars.append(ALPHABET[idx])
    return "".join(chars)


def brute_force_decode(numbers: list[int]) -> list[tuple[int, int, str]]:
    guesses = []
    for a in range(1, 6):
        for b in range(0, 6):
            guesses.append((a, b, decode_numbers(numbers, a, b)))
    return guesses


def brute_force_with_cartesian(numbers: list[int]) -> list[tuple[int, int, str]]:
    params = calc_cartesian_product([list(range(1, 6)), list(range(0, 6))])
    return [(a, b, decode_numbers(numbers, a, b)) for a, b in params]


def is_valid(grid: list[int], magic_sum: int = 15) -> bool:
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]
    for line in lines:
        values = [grid[i] for i in line]
        if 0 not in values and sum(values) != magic_sum:
            return False
    return len(set(x for x in grid if x != 0)) == len([x for x in grid if x != 0])


def solve_magic_square(grid: list[int] | None = None) -> list[int] | None:
    grid = (grid or [0] * 9)[:]
    if 0 not in grid:
        return grid if is_valid(grid) else None
    index = grid.index(0)
    used = set(grid)
    for candidate in range(1, 10):
        if candidate in used:
            continue
        grid[index] = candidate
        if is_valid(grid):
            solved = solve_magic_square(grid)
            if solved is not None:
                return solved
        grid[index] = 0
    return None


def solve_magic_square_stochastic(attempts: int = 2000) -> list[int] | None:
    nums = list(range(1, 10))
    for _ in range(attempts):
        random.shuffle(nums)
        if is_valid(nums) and sum(nums[0:3]) == 15 and sum(nums[3:6]) == 15 and sum(nums[6:9]) == 15:
            return nums[:]
    return solve_magic_square()


def power_rule_derivative(coefficient: float, power: int) -> tuple[float, int]:
    return coefficient * power, power - 1


def bisection_search(fn, left: float, right: float, epsilon: float = 1e-6, max_iters: int = 10_000) -> float:
    f_left = fn(left)
    f_right = fn(right)
    if f_left == 0:
        return left
    if f_right == 0:
        return right
    if f_left * f_right > 0:
        raise ValueError("Bisection requires a sign change on the interval.")
    for _ in range(max_iters):
        mid = (left + right) / 2
        f_mid = fn(mid)
        if abs(f_mid) < epsilon or abs(right - left) < epsilon:
            return mid
        if f_left * f_mid <= 0:
            right, f_right = mid, f_mid
        else:
            left, f_left = mid, f_mid
    return (left + right) / 2


def derivative(fn, x: float, h: float = 1e-5) -> float:
    return (fn(x + h) - fn(x - h)) / (2 * h)


def newton_raphson(fn, fn_prime, x0: float, epsilon: float = 1e-6, max_iters: int = 1000) -> float:
    x = x0
    for _ in range(max_iters):
        slope = fn_prime(x)
        if abs(slope) < epsilon:
            break
        x_new = x - fn(x) / slope
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    return x


def newton_raphson_recursive(fn, fn_prime, x0: float, epsilon: float = 1e-6, max_iters: int = 100) -> float:
    if max_iters <= 0:
        return x0
    slope = fn_prime(x0)
    if abs(slope) < epsilon:
        return x0
    x1 = x0 - fn(x0) / slope
    if abs(x1 - x0) < epsilon:
        return x1
    return newton_raphson_recursive(fn, fn_prime, x1, epsilon, max_iters - 1)


def exact_derivative_quadratic(a: float, b: float, c: float, x: float) -> float:
    return 2 * a * x + b


def gradient_descent_step(x: float, grad: float, alpha: float) -> float:
    return x - alpha * grad


def gradient_descent(f_prime, x0: float, alpha: float = 0.01, epsilon: float = 1e-6, max_iters: int = 10_000) -> float:
    x = x0
    for _ in range(max_iters):
        new_x = x - alpha * f_prime(x)
        if abs(new_x - x) < epsilon:
            return new_x
        x = new_x
    return x


def minimize_via_bisection(f_prime, left: float, right: float, epsilon: float = 1e-6) -> float:
    return bisection_search(f_prime, left, right, epsilon=epsilon)


def dot_product(vec1: list[float], vec2: list[float]) -> float:
    return sum(a * b for a, b in zip(vec1, vec2))


def partial_derivative(fn, point: list[float], index: int, h: float = 1e-5) -> float:
    left = point[:]
    right = point[:]
    left[index] -= h
    right[index] += h
    return (fn(right) - fn(left)) / (2 * h)


def gradient(fn, point: list[float], h: float = 1e-5) -> list[float]:
    return [partial_derivative(fn, point, i, h=h) for i in range(len(point))]


def multivariable_gd(fn, start: list[float], alpha: float = 0.05, epsilon: float = 1e-6, max_iters: int = 5000) -> list[float]:
    point = start[:]
    for _ in range(max_iters):
        grad = gradient(fn, point)
        new_point = [x - alpha * g for x, g in zip(point, grad)]
        if math.dist(new_point, point) < epsilon:
            return new_point
        point = new_point
    return point


def global_minimum_search(fn, starts: list[list[float]], alpha: float = 0.05) -> tuple[list[float], float]:
    best_point = None
    best_value = float("inf")
    for start in starts:
        point = multivariable_gd(fn, start, alpha=alpha)
        value = fn(point)
        if value < best_value:
            best_point, best_value = point, value
    return best_point or starts[0], best_value


def selection_sort(values: list[int]) -> list[int]:
    arr = values[:]
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(values: list[int]) -> list[int]:
    arr = values[:]
    for end in range(len(arr) - 1, 0, -1):
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def insertion_sort(values: list[int]) -> list[int]:
    arr = values[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def counting_sort(values: list[int]) -> list[int]:
    if not values:
        return []
    lo, hi = min(values), max(values)
    counts = [0] * (hi - lo + 1)
    for value in values:
        counts[value - lo] += 1
    out = []
    for index, count in enumerate(counts):
        out.extend([index + lo] * count)
    return out


def sort_simulated_data(size: int = 25) -> dict[str, list[int]]:
    data = [random.randint(0, 50) for _ in range(size)]
    return {
        "original": data,
        "selection": selection_sort(data),
        "bubble": bubble_sort(data),
        "insertion": insertion_sort(data),
        "counting": counting_sort(data),
    }


def merge(left: list[int], right: list[int]) -> list[int]:
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return values[:]
    mid = len(values) // 2
    return merge(merge_sort(values[:mid]), merge_sort(values[mid:]))


def partition(arr: list[int], low: int = 0, high: int | None = None) -> tuple[list[int], int]:
    data = arr[:]
    high = len(data) - 1 if high is None else high
    pivot = data[high]
    i = low
    for j in range(low, high):
        if data[j] <= pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[high] = data[high], data[i]
    return data, i


def quicksort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return values[:]
    pivot = values[len(values) // 2]
    left = [x for x in values if x < pivot]
    middle = [x for x in values if x == pivot]
    right = [x for x in values if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def binary_search(values: list[int], target: int) -> int:
    left, right = 0, len(values) - 1
    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def vector_norm(vec: list[float]) -> float:
    return math.sqrt(sum(x * x for x in vec))


def matrix_add(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]


def matrix_multiply(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    cols = list(zip(*B))
    return [[dot_product(row, list(col)) for col in cols] for row in A]


def determinant(A: list[list[float]]) -> float:
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    total = 0.0
    for col, value in enumerate(A[0]):
        minor = [row[:col] + row[col + 1:] for row in A[1:]]
        total += ((-1) ** col) * value * determinant(minor)
    return total


def eliminate_variable(eq1: list[float], eq2: list[float], index: int = 0) -> list[float]:
    if eq2[index] == 0:
        return eq2[:]
    factor = eq1[index] / eq2[index]
    return [a - factor * b for a, b in zip(eq1, eq2)]


def swap_rows(matrix: list[list[float]], i: int, j: int) -> list[list[float]]:
    M = [row[:] for row in matrix]
    M[i], M[j] = M[j], M[i]
    return M


def scale_row(row: list[float], scalar: float) -> list[float]:
    return [value * scalar for value in row]


def rref(matrix: list[list[float]]) -> list[list[float]]:
    A = np.array(matrix, dtype=float)
    rows, cols = A.shape
    pivot_row = 0
    for pivot_col in range(cols):
        if pivot_row >= rows:
            break
        pivot = None
        for r in range(pivot_row, rows):
            if abs(A[r, pivot_col]) > 1e-10:
                pivot = r
                break
        if pivot is None:
            continue
        if pivot != pivot_row:
            A[[pivot_row, pivot]] = A[[pivot, pivot_row]]
        A[pivot_row] = A[pivot_row] / A[pivot_row, pivot_col]
        for r in range(rows):
            if r != pivot_row:
                A[r] -= A[r, pivot_col] * A[pivot_row]
        pivot_row += 1
    return A.round(10).tolist()


def inverse(matrix: list[list[float]]) -> list[list[float]]:
    return np.linalg.inv(np.array(matrix, dtype=float)).tolist()


def distance(point_a: list[float], point_b: list[float]) -> float:
    return math.dist(point_a, point_b)


def assign_clusters(points: list[list[float]], centroids: list[list[float]]) -> list[int]:
    labels = []
    for point in points:
        labels.append(min(range(len(centroids)), key=lambda idx: distance(point, centroids[idx])))
    return labels


def k_means(points: list[list[float]], k: int, iters: int = 20) -> tuple[list[list[float]], list[int]]:
    centroids = [point[:] for point in points[:k]]
    labels = [0] * len(points)
    for _ in range(iters):
        labels = assign_clusters(points, centroids)
        new_centroids = []
        for cluster_id in range(k):
            cluster_points = [point for point, label in zip(points, labels) if label == cluster_id]
            if cluster_points:
                new_centroids.append(np.mean(cluster_points, axis=0).tolist())
            else:
                new_centroids.append(centroids[cluster_id])
        if all(distance(a, b) < 1e-9 for a, b in zip(centroids, new_centroids)):
            break
        centroids = new_centroids
    return centroids, labels


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def available_moves(self) -> list[int]:
        return [i for i, value in enumerate(self.board) if value == " "]

    def make_move(self, index: int) -> bool:
        if self.board[index] != " ":
            return False
        self.board[index] = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def winner(self) -> str | None:
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]
        for a, b, c in lines:
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_draw(self) -> bool:
        return self.winner() is None and not self.available_moves()

    def display(self) -> str:
        rows = [" | ".join(self.board[i:i + 3]) for i in range(0, 9, 3)]
        return "\n---------\n".join(rows)


class ConnectFour:
    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.board = [[" "] * cols for _ in range(rows)]
        self.current_player = "X"

    def available_moves(self) -> list[int]:
        return [c for c in range(self.cols) if self.board[0][c] == " "]

    def make_move(self, col: int) -> bool:
        if col not in self.available_moves():
            return False
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == " ":
                self.board[row][col] = self.current_player
                self.current_player = "O" if self.current_player == "X" else "X"
                return True
        return False

    def winner(self) -> str | None:
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for r in range(self.rows):
            for c in range(self.cols):
                token = self.board[r][c]
                if token == " ":
                    continue
                for dr, dc in directions:
                    cells = []
                    for step in range(4):
                        nr, nc = r + dr * step, c + dc * step
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            cells.append(self.board[nr][nc])
                    if len(cells) == 4 and all(cell == token for cell in cells):
                        return token
        return None

    def is_draw(self) -> bool:
        return self.winner() is None and not self.available_moves()

    def display(self) -> str:
        return "\n".join("|".join(row) for row in self.board)


def random_game_loop(game) -> dict[str, Any]:
    history = []
    while getattr(game, "winner")() is None and not getattr(game, "is_draw")():
        move = random.choice(game.available_moves())
        history.append((getattr(game, "current_player"), move))
        game.make_move(move)
    return {"winner": game.winner(), "draw": game.is_draw(), "history": history}


def instantaneous_rate_of_change(fn, t: float, h: float = 1e-5) -> float:
    return (fn(t + h) - fn(t)) / h


def euler_estimation(f, x0: float, y0: float, step: float, n_steps: int) -> list[tuple[float, float]]:
    x, y = x0, y0
    out = [(x, y)]
    for _ in range(n_steps):
        y += step * f(x, y)
        x += step
        out.append((x, y))
    return out


def multivariable_euler(fns, t0: float, state0: list[float], step: float, n_steps: int) -> list[tuple[float, list[float]]]:
    t = t0
    state = state0[:]
    out = [(t, state[:])]
    for _ in range(n_steps):
        derivatives = fns(t, state)
        state = [value + step * deriv for value, deriv in zip(state, derivatives)]
        t += step
        out.append((t, state[:]))
    return out


def dS_dt(S: float, I: float, beta: float, N: float) -> float:
    return -beta * S * I / N


def dI_dt(S: float, I: float, beta: float, gamma: float, N: float) -> float:
    return beta * S * I / N - gamma * I


def dR_dt(I: float, gamma: float) -> float:
    return gamma * I


def simulate_sir(S0: float, I0: float, R0: float, beta: float, gamma: float, dt: float, steps: int) -> list[tuple[float, float, float]]:
    N = S0 + I0 + R0
    S, I, R = S0, I0, R0
    out = [(S, I, R)]
    for _ in range(steps):
        S += dt * dS_dt(S, I, beta, N)
        I += dt * dI_dt(S, I, beta, gamma, N)
        R += dt * dR_dt(I, gamma)
        out.append((S, I, R))
    return out


def optimize_sir_params(observed_peak: float, candidates: list[tuple[float, float]], S0: float = 999.0, I0: float = 1.0, R0: float = 0.0) -> tuple[float, float]:
    best = candidates[0]
    best_error = float("inf")
    for beta, gamma in candidates:
        peak = max(I for _, I, _ in simulate_sir(S0, I0, R0, beta, gamma, 0.1, 200))
        error = abs(peak - observed_peak)
        if error < best_error:
            best, best_error = (beta, gamma), error
    return best


def I_Na(V: float, m: float, h: float, g_na: float = 120.0, E_na: float = 115.0) -> float:
    return g_na * (m ** 3) * h * (V - E_na)


def I_K(V: float, n: float, g_k: float = 36.0, E_k: float = -12.0) -> float:
    return g_k * (n ** 4) * (V - E_k)


def simulate_neuron(T: float = 20.0, dt: float = 0.01, stimulus: float = 10.0) -> list[float]:
    V = 0.0
    m = 0.05
    h = 0.6
    n = 0.32
    trace = []
    for _ in range(int(T / dt)):
        dv = stimulus - I_Na(V, m, h) - I_K(V, n) - 0.3 * (V - 10.6)
        V += dt * dv / 1.0
        m = min(max(m + dt * (0.1 * (1 - m) - 0.05 * m), 0.0), 1.0)
        h = min(max(h + dt * (0.07 * (1 - h) - 0.01 * h), 0.0), 1.0)
        n = min(max(n + dt * (0.01 * (1 - n) - 0.02 * n), 0.0), 1.0)
        trace.append(V)
    return trace


def hash_string(string: str, num_buckets: int) -> int:
    return sum(ord(ch) for ch in string) % num_buckets


class HashTable:
    def __init__(self, num_buckets: int = 8):
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]

    def set(self, key: str, value: Any) -> None:
        bucket = self.buckets[hash_string(key, self.num_buckets)]
        for item in bucket:
            if item[0] == key:
                item[1] = value
                return
        bucket.append([key, value])

    def get(self, key: str, default: Any = None) -> Any:
        bucket = self.buckets[hash_string(key, self.num_buckets)]
        for k, value in bucket:
            if k == key:
                return value
        return default

    def items(self) -> list[tuple[str, Any]]:
        return [(key, value) for bucket in self.buckets for key, value in bucket]


def count_characters_hashed(string: str) -> HashTable:
    table = HashTable()
    for ch in string.lower():
        table.set(ch, (table.get(ch, 0) or 0) + 1)
    return table


def satisfies_inequalities(point: list[float], constraints: list[tuple[list[float], float]]) -> bool:
    return all(dot_product(coeffs, point) <= bound + 1e-9 for coeffs, bound in constraints)


def add_slack_variables(constraints: list[tuple[list[float], float]]) -> list[list[float]]:
    rows = []
    for i, (coeffs, bound) in enumerate(constraints):
        slack = [0.0] * len(constraints)
        slack[i] = 1.0
        rows.append([*coeffs, *slack, float(bound)])
    return rows


def simplex_pivot(tableau: list[list[float]], pivot_row: int, pivot_col: int) -> list[list[float]]:
    T = np.array(tableau, dtype=float)
    T[pivot_row] = T[pivot_row] / T[pivot_row, pivot_col]
    for row in range(len(T)):
        if row != pivot_row:
            T[row] -= T[row, pivot_col] * T[pivot_row]
    return T.tolist()


def simplex_method(objective: list[float], constraints: list[tuple[list[float], float]]) -> dict[str, Any]:
    m = len(constraints)
    n = len(objective)
    tableau = add_slack_variables(constraints)
    tableau.append([-value for value in objective] + [0.0] * m + [0.0])
    while True:
        last = tableau[-1]
        pivot_col = min(range(n + m), key=lambda idx: last[idx])
        if last[pivot_col] >= -1e-9:
            break
        ratios = []
        for row in range(m):
            entry = tableau[row][pivot_col]
            if entry > 1e-9:
                ratios.append((tableau[row][-1] / entry, row))
        if not ratios:
            raise ValueError("Unbounded objective.")
        _, pivot_row = min(ratios)
        tableau = simplex_pivot(tableau, pivot_row, pivot_col)
    solution = [0.0] * n
    for col in range(n):
        pivot_row = None
        for row in range(m):
            if abs(tableau[row][col] - 1.0) < 1e-9 and all(abs(tableau[r][col]) < 1e-9 for r in range(m) if r != row):
                pivot_row = row
                break
        if pivot_row is not None:
            solution[col] = tableau[pivot_row][-1]
    return {"solution": solution, "value": tableau[-1][-1], "tableau": tableau}


def pseudoinverse(X: list[list[float]]) -> list[list[float]]:
    matrix = np.array(X, dtype=float)
    return np.linalg.pinv(matrix).tolist()


def polynomial_regression(x: list[float], y: list[float], degree: int) -> list[float]:
    X = np.vander(x, degree + 1, increasing=True)
    coeffs = np.linalg.pinv(X) @ np.array(y, dtype=float)
    return coeffs.tolist()


def transform_exponential(x: list[float], y: list[float]) -> tuple[float, float]:
    mask = [value > 0 for value in y]
    x_valid = np.array([value for value, keep in zip(x, mask) if keep], dtype=float)
    y_valid = np.log([value for value in y if value > 0])
    X = np.vstack([np.ones(len(x_valid)), x_valid]).T
    a0, a1 = np.linalg.pinv(X) @ y_valid
    return float(math.exp(a0)), float(a1)


def transform_logistic(x: list[float], y: list[float]) -> tuple[float, float]:
    y_arr = np.clip(np.array(y, dtype=float), 1e-6, 1 - 1e-6)
    logit = np.log(y_arr / (1 - y_arr))
    X = np.vstack([np.ones(len(x)), np.array(x, dtype=float)]).T
    a0, a1 = np.linalg.pinv(X) @ logit
    return float(a0), float(a1)


def nonlinear_regression(x: list[float], y: list[float], model: str = "polynomial", degree: int = 2) -> Any:
    if model == "polynomial":
        return polynomial_regression(x, y, degree)
    if model == "exponential":
        return transform_exponential(x, y)
    if model == "logistic":
        return transform_logistic(x, y)
    raise ValueError(f"Unknown model: {model}")


def train_test_split(X: list[Any], y: list[Any], test_ratio: float = 0.2, seed: int = 42):
    indices = list(range(len(X)))
    random.Random(seed).shuffle(indices)
    cut = int(len(indices) * (1 - test_ratio))
    train_idx, test_idx = indices[:cut], indices[cut:]
    X_train = [X[i] for i in train_idx]
    y_train = [y[i] for i in train_idx]
    X_test = [X[i] for i in test_idx]
    y_test = [y[i] for i in test_idx]
    return X_train, X_test, y_train, y_test


def compute_mse(y_true: list[float], y_pred: list[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(y_true, y_pred)) / len(y_true)


def k_fold_cross_validation(model_fn, X: list[Any], y: list[float], k: int = 5) -> float:
    fold_size = max(1, len(X) // k)
    scores = []
    for fold in range(k):
        start = fold * fold_size
        stop = min(len(X), start + fold_size)
        X_test = X[start:stop]
        y_test = y[start:stop]
        X_train = X[:start] + X[stop:]
        y_train = y[:start] + y[stop:]
        predictor = model_fn(X_train, y_train)
        predictions = [predictor(x) for x in X_test]
        scores.append(compute_mse(y_test, predictions))
    return sum(scores) / len(scores)


def mse_gradient(X: list[list[float]], y: list[float], weights: list[float]) -> list[float]:
    X_arr = np.array(X, dtype=float)
    y_arr = np.array(y, dtype=float)
    w_arr = np.array(weights, dtype=float)
    preds = X_arr @ w_arr
    grad = 2 / len(X_arr) * (X_arr.T @ (preds - y_arr))
    return grad.tolist()


def multiple_regression_gd(X: list[list[float]], y: list[float], alpha: float = 0.01, epochs: int = 1000) -> list[float]:
    weights = np.zeros(len(X[0]), dtype=float)
    for _ in range(epochs):
        grad = np.array(mse_gradient(X, y, weights.tolist()))
        weights -= alpha * grad
    return weights.tolist()


def add_interaction_terms(X: list[list[float]]) -> list[list[float]]:
    out = []
    for row in X:
        interactions = [row[i] * row[j] for i in range(len(row)) for j in range(i + 1, len(row))]
        out.append(row + interactions)
    return out


def optimize_weights_gd(X: list[list[float]], y: list[float], alphas: list[float], epochs: int = 1000) -> tuple[float, list[float]]:
    best_alpha = alphas[0]
    best_weights = multiple_regression_gd(X, y, alpha=best_alpha, epochs=epochs)
    best_error = compute_mse(y, (np.array(X) @ np.array(best_weights)).tolist())
    for alpha in alphas[1:]:
        weights = multiple_regression_gd(X, y, alpha=alpha, epochs=epochs)
        error = compute_mse(y, (np.array(X) @ np.array(weights)).tolist())
        if error < best_error:
            best_alpha, best_weights, best_error = alpha, weights, error
    return best_alpha, best_weights


def get_neighbors(X_train: list[list[float]], y_train: list[Any], query: list[float], k: int) -> list[tuple[float, Any]]:
    pairs = []
    for point, label in zip(X_train, y_train):
        pairs.append((distance(point, query), label))
    pairs.sort(key=lambda item: item[0])
    return pairs[:k]


def knn_classify(X_train: list[list[float]], y_train: list[Any], query: list[float], k: int = 3) -> Any:
    neighbors = get_neighbors(X_train, y_train, query, k)
    return Counter(label for _, label in neighbors).most_common(1)[0][0]


def compute_probabilities(rows: list[list[Any]], labels: list[Any]) -> dict[str, Any]:
    class_counts = Counter(labels)
    total = len(labels)
    probabilities: dict[str, Any] = {"class_priors": {label: count / total for label, count in class_counts.items()}, "feature_counts": {}}
    for label in class_counts:
        probabilities["feature_counts"][label] = Counter()
    for row, label in zip(rows, labels):
        probabilities["feature_counts"][label].update(row)
    return probabilities


def naive_bayes_classify(rows: list[list[Any]], labels: list[Any], query: list[Any]) -> Any:
    model = compute_probabilities(rows, labels)
    vocab = set(item for row in rows for item in row)
    scores = {}
    for label, prior in model["class_priors"].items():
        total_words = sum(model["feature_counts"][label].values())
        score = math.log(prior)
        for token in query:
            count = model["feature_counts"][label][token]
            score += math.log((count + 1) / (total_words + len(vocab)))
        scores[label] = score
    return max(scores, key=scores.get)


def bfs(graph: dict[Any, list[Any]], start: Any) -> list[Any]:
    visited = []
    queue = deque([start])
    seen = {start}
    while queue:
        node = queue.popleft()
        visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return visited


def dfs_iterative(graph: dict[Any, list[Any]], start: Any) -> list[Any]:
    visited = []
    stack = [start]
    seen = set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        visited.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return visited


def dfs_recursive(graph: dict[Any, list[Any]], start: Any, seen: set[Any] | None = None, visited: list[Any] | None = None) -> list[Any]:
    seen = seen or set()
    visited = visited or []
    seen.add(start)
    visited.append(start)
    for neighbor in graph.get(start, []):
        if neighbor not in seen:
            dfs_recursive(graph, neighbor, seen, visited)
    return visited


def find_connected_components(graph: dict[Any, list[Any]]) -> list[list[Any]]:
    seen = set()
    components = []
    for node in graph:
        if node not in seen:
            component = bfs(graph, node)
            seen.update(component)
            components.append(component)
    return components


class PriorityQueue:
    def __init__(self):
        self._heap: list[tuple[float, Any]] = []

    def push(self, priority: float, item: Any) -> None:
        heapq.heappush(self._heap, (priority, item))

    def pop(self) -> tuple[float, Any]:
        return heapq.heappop(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)


def dijkstra(graph: dict[Any, list[tuple[Any, float]]], start_node: Any) -> tuple[dict[Any, float], dict[Any, Any | None]]:
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[start_node] = 0.0
    pq = PriorityQueue()
    pq.push(0.0, start_node)
    while pq:
        current_dist, node = pq.pop()
        if current_dist > distances[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            new_dist = current_dist + weight
            if new_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_dist
                previous[neighbor] = node
                pq.push(new_dist, neighbor)
    return distances, previous


def unweighted_shortest_path_bfs(graph: dict[Any, list[Any]], start_node: Any) -> dict[Any, int]:
    distances = {start_node: 0}
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances


def safe_p_log_p(p: float) -> float:
    return 0.0 if p <= 0 else p * math.log2(p)


def calculate_entropy(labels: list[Any]) -> float:
    counts = Counter(labels)
    total = len(labels)
    return -sum(safe_p_log_p(count / total) for count in counts.values())


def information_gain(rows: list[dict[str, Any]], feature: str, target: str) -> float:
    base = calculate_entropy([row[target] for row in rows])
    groups: dict[Any, list[dict[str, Any]]] = {}
    for row in rows:
        groups.setdefault(row[feature], []).append(row)
    weighted = 0.0
    for group in groups.values():
        weighted += len(group) / len(rows) * calculate_entropy([row[target] for row in group])
    return base - weighted


def build_decision_tree(rows: list[dict[str, Any]], target: str, features: list[str] | None = None) -> Any:
    labels = [row[target] for row in rows]
    if len(set(labels)) == 1:
        return labels[0]
    features = features or [key for key in rows[0] if key != target]
    if not features:
        return Counter(labels).most_common(1)[0][0]
    best_feature = max(features, key=lambda feat: information_gain(rows, feat, target))
    tree: dict[Any, Any] = {"feature": best_feature, "branches": {}}
    for value in {row[best_feature] for row in rows}:
        subset = [row for row in rows if row[best_feature] == value]
        remaining = [feat for feat in features if feat != best_feature]
        tree["branches"][value] = build_decision_tree(subset, target, remaining)
    return tree


def print_tree_dfs(tree: Any, indent: str = "") -> None:
    if not isinstance(tree, dict):
        print(indent + f"-> {tree}")
        return
    print(indent + f"[{tree['feature']}]")
    for value, branch in tree["branches"].items():
        print(indent + f"  {value}:")
        print_tree_dfs(branch, indent + "    ")


def chain_rule_gradient(df_dg: float, dg_dx: float) -> float:
    return df_dg * dg_dx


def _sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward_pass(inputs, weights, biases):
    activations = np.array(inputs, dtype=float)
    layer_outputs = []
    for W, b in zip(weights, biases):
        z = activations @ np.array(W, dtype=float) + np.array(b, dtype=float)
        activations = _sigmoid(z)
        layer_outputs.append(activations.copy())
    return layer_outputs


def backpropagation(inputs, outputs, target, weights, biases):
    x = np.array(inputs, dtype=float)
    activations = [x]
    zs = []
    for W, b in zip(weights, biases):
        z = activations[-1] @ np.array(W, dtype=float) + np.array(b, dtype=float)
        zs.append(z)
        activations.append(_sigmoid(z))
    target_arr = np.array(target, dtype=float)
    delta = (activations[-1] - target_arr) * activations[-1] * (1 - activations[-1])
    grad_w = [None] * len(weights)
    grad_b = [None] * len(biases)
    grad_w[-1] = np.outer(activations[-2], delta)
    grad_b[-1] = delta
    for layer in range(len(weights) - 2, -1, -1):
        delta = (np.array(weights[layer + 1], dtype=float) @ delta) * activations[layer + 1] * (1 - activations[layer + 1])
        grad_w[layer] = np.outer(activations[layer], delta)
        grad_b[layer] = delta
    return [g.tolist() for g in grad_w], [g.tolist() for g in grad_b]


def train_network(X, Y, epochs, alpha):
    X_arr = np.array(X, dtype=float)
    Y_arr = np.array(Y, dtype=float).reshape(len(X), -1)
    weights = [
        np.random.uniform(-0.5, 0.5, size=(X_arr.shape[1], 2)),
        np.random.uniform(-0.5, 0.5, size=(2, Y_arr.shape[1])),
    ]
    biases = [
        np.zeros(2),
        np.zeros(Y_arr.shape[1]),
    ]
    for _ in range(epochs):
        for x, y in zip(X_arr, Y_arr):
            grad_w, grad_b = backpropagation(x, None, y, [w.tolist() for w in weights], [b.tolist() for b in biases])
            weights = [w - alpha * np.array(gw) for w, gw in zip(weights, grad_w)]
            biases = [b - alpha * np.array(gb) for b, gb in zip(biases, grad_b)]
    return [w.tolist() for w in weights], [b.tolist() for b in biases]


def minimax(state, player, moves_fn, terminal_fn, evaluate_fn):
    terminal, value = terminal_fn(state)
    if terminal:
        return value
    children = [moves_fn(state, move, player) for move in moves_fn(state)]
    if player == 1:
        return max(minimax(child, -1, moves_fn, terminal_fn, evaluate_fn) for child in children)
    return min(minimax(child, 1, moves_fn, terminal_fn, evaluate_fn) for child in children)


def alphabeta(state, depth, alpha, beta, maximizing_player, children_fn, terminal_fn, evaluate_fn):
    terminal, value = terminal_fn(state)
    if depth == 0 or terminal:
        return value if terminal else evaluate_fn(state)
    if maximizing_player:
        best = -float("inf")
        for child in children_fn(state):
            best = max(best, alphabeta(child, depth - 1, alpha, beta, False, children_fn, terminal_fn, evaluate_fn))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    best = float("inf")
    for child in children_fn(state):
        best = min(best, alphabeta(child, depth - 1, alpha, beta, True, children_fn, terminal_fn, evaluate_fn))
        beta = min(beta, best)
        if beta <= alpha:
            break
    return best


def evaluate_connect_four(board: list[list[str]], player: str = "X") -> int:
    opponent = "O" if player == "X" else "X"
    score = 0
    center_column = [row[len(board[0]) // 2] for row in board]
    score += center_column.count(player) * 3
    score -= center_column.count(opponent) * 2
    return score


def evaluate_relative_fitness(population: list[np.ndarray], board_fn) -> list[float]:
    scores = []
    for weights in population:
        scores.append(float(board_fn(weights)))
    return scores


def evaluate_board_mlp(board: list[float], weights: np.ndarray) -> float:
    board_arr = np.array(board, dtype=float)
    return float(np.tanh(board_arr @ weights))


def evolve_population_tournament(population: list[np.ndarray], fitness_fn, generations: int = 10, mutation_scale: float = 0.1) -> list[np.ndarray]:
    current = [np.array(individual, dtype=float) for individual in population]
    for _ in range(generations):
        scored = sorted(((fitness_fn(individual), individual) for individual in current), key=lambda item: item[0], reverse=True)
        survivors = [individual for _, individual in scored[: max(2, len(scored) // 2)]]
        children = [individual + np.random.normal(scale=mutation_scale, size=individual.shape) for individual in survivors]
        current = survivors + children
    return current


def train_blondie24_agent(board_size: int = 9, population_size: int = 8, generations: int = 5) -> np.ndarray:
    population = [np.random.uniform(-1, 1, size=board_size) for _ in range(population_size)]
    evolved = evolve_population_tournament(population, lambda w: float(np.sum(np.abs(w))), generations=generations)
    return evolved[0]


def apply_convolution_2d(matrix: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
    data = np.array(matrix, dtype=float)
    filt = np.array(kernel, dtype=float)
    out_rows = data.shape[0] - filt.shape[0] + 1
    out_cols = data.shape[1] - filt.shape[1] + 1
    out = np.zeros((out_rows, out_cols))
    for r in range(out_rows):
        for c in range(out_cols):
            out[r, c] = float(np.sum(data[r:r + filt.shape[0], c:c + filt.shape[1]] * filt))
    return out.tolist()


def max_pooling_2d(matrix: list[list[float]], pool_size: int = 2, stride: int = 2) -> list[list[float]]:
    data = np.array(matrix, dtype=float)
    out_rows = 1 + (data.shape[0] - pool_size) // stride
    out_cols = 1 + (data.shape[1] - pool_size) // stride
    out = np.zeros((out_rows, out_cols))
    for r in range(out_rows):
        for c in range(out_cols):
            window = data[r * stride:r * stride + pool_size, c * stride:c * stride + pool_size]
            out[r, c] = np.max(window)
    return out.tolist()


def evaluate_board_cnn(board: list[list[float]], kernel: list[list[float]], dense_weights: list[float]) -> float:
    convolved = apply_convolution_2d(board, kernel)
    pooled = max_pooling_2d(convolved)
    flat = np.array(pooled, dtype=float).flatten()
    weights = np.array(dense_weights[: len(flat)], dtype=float)
    return float(flat @ weights)


def train_convolutional_blondie24(board_shape: tuple[int, int] = (6, 7), generations: int = 5) -> dict[str, Any]:
    kernel = np.random.uniform(-1, 1, size=(2, 2))
    dense = np.random.uniform(-1, 1, size=(int((board_shape[0] - 1) / 2) * int((board_shape[1] - 1) / 2),))
    for _ in range(generations):
        kernel += np.random.normal(scale=0.05, size=kernel.shape)
        dense += np.random.normal(scale=0.05, size=dense.shape)
    return {"kernel": kernel.tolist(), "dense_weights": dense.tolist()}


def solve_linear(a: float, b: float, c: float) -> float:
    if a == 0:
        raise ValueError("a must be nonzero")
    return (c - b) / a


def solve_complex_linear(a: float, b: float, c: float, d: float = 0.0) -> float:
    return solve_linear(a, b + d, c)


def verify_solution(a: float, b: float, c: float, x: float) -> bool:
    return abs(a * x + b - c) < 1e-9


def difference_quotient(fn, x: float, h: float) -> float:
    return (fn(x + h) - fn(x)) / h


def exact_derivative(coefficients: list[float]) -> list[float]:
    return [power * coefficient for power, coefficient in enumerate(coefficients[1:], start=1)]


def inner_g_prime(x: float) -> float:
    return 2 * x


def outer_f_prime(u: float) -> float:
    return 3 * (u ** 2)


def chain_rule(x: float) -> float:
    return outer_f_prime(x ** 2) * inner_g_prime(x)


def find_minimum_vertex(a: float, b: float, c: float) -> tuple[float, float]:
    x = -b / (2 * a)
    y = a * x * x + b * x + c
    return x, y


def bisection_root_finding(fn, left: float, right: float, epsilon: float = 1e-6) -> float:
    return bisection_search(fn, left, right, epsilon=epsilon)


def vector_add(vec1: list[float], vec2: list[float]) -> list[float]:
    return [a + b for a, b in zip(vec1, vec2)]


def vector_angle(vec1: list[float], vec2: list[float]) -> float:
    denom = vector_norm(vec1) * vector_norm(vec2)
    if denom == 0:
        raise ValueError("Vectors must be nonzero.")
    cosine = max(-1.0, min(1.0, dot_product(vec1, vec2) / denom))
    return math.degrees(math.acos(cosine))


def matrix_vector_mult(A: list[list[float]], v: list[float]) -> list[float]:
    return [dot_product(row, v) for row in A]


def matrix_mult(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    return matrix_multiply(A, B)


def euler_population(P0: float, growth_rate: float, dt: float, steps: int) -> list[float]:
    P = P0
    out = [P]
    for _ in range(steps):
        P += dt * growth_rate * P
        out.append(P)
    return out

