"""Replace legacy solution notebook placeholders with real implementations."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "mathematics" / "solutions"
PLACEHOLDER = "TODO: Reference instructor solution implementation here"


def code(*lines: str) -> str:
    return "\n".join(lines).strip()


REPLACEMENTS = {
    "01_introductory_coding.ipynb": [
        code("from curriculum.legacy_solution_bank import check_if_symmetric", "", "print(check_if_symmetric('racecar'))", "print(check_if_symmetric('hello'))"),
        code("from curriculum.legacy_solution_bank import count_characters", "", "print(count_characters('racecar'))"),
        code("from curriculum.legacy_solution_bank import is_prime", "", "print(is_prime(7))", "print(is_prime(10))"),
        code("from curriculum.legacy_solution_bank import symmetric_prime_counts", "", "print(symmetric_prime_counts('racecar'))"),
        code("from curriculum.legacy_solution_bank import check_if_symmetric, is_prime", "", "symmetric_primes = [n for n in range(2, 200) if is_prime(n) and check_if_symmetric(str(n))]", "print(symmetric_primes)"),
    ],
    "02_number_systems.ipynb": [
        code("from curriculum.legacy_solution_bank import binary_to_decimal", "", "print(binary_to_decimal('11010'))"),
        code("from curriculum.legacy_solution_bank import decimal_to_hexadecimal", "", "print(decimal_to_hexadecimal('255'))"),
        code("from curriculum.legacy_solution_bank import binary_to_hexadecimal", "", "print(binary_to_hexadecimal('11111111'))"),
        code("from curriculum.legacy_solution_bank import is_binary_symmetric", "", "print(is_binary_symmetric('9'))"),
        code("from curriculum.legacy_solution_bank import binary_to_decimal, decimal_to_hexadecimal", "", "for bits in ['1010', '1111', '100000']:", "    print(bits, '->', binary_to_decimal(bits), '->', decimal_to_hexadecimal(binary_to_decimal(bits)))"),
    ],
    "03_recursive_sequences.ipynb": [
        code("from curriculum.legacy_solution_bank import fibonacci_iterative", "", "print(fibonacci_iterative(10))"),
        code("from curriculum.legacy_solution_bank import fibonacci_recursive", "", "print(fibonacci_recursive(10))"),
        code("from curriculum.legacy_solution_bank import collatz_sequence", "", "print(collatz_sequence(13))"),
        code("from curriculum.legacy_solution_bank import count_prime_collatz", "", "print(count_prime_collatz(13))"),
        code("from curriculum.legacy_solution_bank import fibonacci_iterative, fibonacci_recursive", "", "pairs = [(n, fibonacci_iterative(n), fibonacci_recursive(n)) for n in range(8)]", "print(pairs)"),
    ],
    "04_simulating_randomness.ipynb": [
        code("from curriculum.legacy_solution_bank import flip_coin", "", "print([flip_coin() for _ in range(10)])"),
        code("from curriculum.legacy_solution_bank import sim_probability, flip_coin", "", "print(sim_probability(1000, lambda: flip_coin() == 1))"),
        code("from curriculum.legacy_solution_bank import average_binary_flips", "", "print(average_binary_flips(1000, target_flips=8))"),
        code("import random, math", "", "inside = 0", "trials = 5000", "for _ in range(trials):", "    x, y = random.random(), random.random()", "    inside += x * x + y * y <= 1", "print('pi estimate:', 4 * inside / trials)"),
    ],
    "05_roulette_wheel.ipynb": [
        code("from curriculum.legacy_solution_bank import get_cumulative_distribution", "", "print(get_cumulative_distribution([0.1, 0.2, 0.7]))"),
        code("from curriculum.legacy_solution_bank import sample_index", "", "print([sample_index([0.1, 0.2, 0.7]) for _ in range(10)])"),
        code("from curriculum.legacy_solution_bank import verify_distribution", "", "print(verify_distribution([0.1, 0.2, 0.7], trials=5000))"),
        code("from curriculum.legacy_solution_bank import sample_index", "", "weights = [1, 3, 6]", "counts = [0, 0, 0]", "for _ in range(5000):", "    counts[sample_index([w / sum(weights) for w in weights])] += 1", "print(counts)"),
    ],
    "06_cartesian_product.ipynb": [
        code("from curriculum.legacy_solution_bank import cartesian_product_2d", "", "print(cartesian_product_2d([1, 2], ['a', 'b']))"),
        code("from curriculum.legacy_solution_bank import calc_cartesian_product", "", "print(calc_cartesian_product([[1, 2], ['a', 'b'], [True, False]]))"),
        code("from curriculum.legacy_solution_bank import sample_from_cartesian", "", "print(sample_from_cartesian([[1, 2], ['a', 'b'], [True, False]]))"),
        code("from curriculum.legacy_solution_bank import calc_cartesian_product", "", "binary_strings = calc_cartesian_product([[0, 1]] * 4)", "print(binary_strings)"),
    ],
    "07_brute_force_crypto.ipynb": [
        code("from curriculum.legacy_solution_bank import algebraic_inverse", "", "print(algebraic_inverse(17, 3, 2))"),
        code("from curriculum.legacy_solution_bank import encode_string", "", "print(encode_string('cab', 3, 2))"),
        code("from curriculum.legacy_solution_bank import decode_numbers, brute_force_decode", "", "encoded = [8, 2, 5]", "print(decode_numbers(encoded, 3, 2))", "print(brute_force_decode(encoded)[:5])"),
        code("from curriculum.legacy_solution_bank import brute_force_with_cartesian", "", "print(brute_force_with_cartesian([8, 2, 5])[:5])"),
        code("from curriculum.legacy_solution_bank import encode_string, brute_force_decode", "", "secret = encode_string('math', 2, 1)", "print(secret)", "print(brute_force_decode(secret)[:10])"),
    ],
    "08_backtracking_magic_squares.ipynb": [
        code("from curriculum.legacy_solution_bank import is_valid", "", "print(is_valid([8, 1, 6, 3, 5, 7, 4, 9, 2]))"),
        code("from curriculum.legacy_solution_bank import solve_magic_square", "", "print(solve_magic_square())"),
        code("from curriculum.legacy_solution_bank import solve_magic_square_stochastic", "", "print(solve_magic_square_stochastic())"),
        code("from curriculum.legacy_solution_bank import solve_magic_square", "", "solution = solve_magic_square()", "grid = [solution[i:i+3] for i in range(0, 9, 3)]", "print(grid)"),
    ],
    "09_estimating_roots.ipynb": [
        code("from curriculum.legacy_solution_bank import power_rule_derivative", "", "print(power_rule_derivative(7, 3))"),
        code("from curriculum.legacy_solution_bank import bisection_search", "", "print(bisection_search(lambda x: x * x - 2, 1, 2))"),
        code("from curriculum.legacy_solution_bank import derivative", "", "print(derivative(lambda x: x ** 3, 2.0))"),
        code("from curriculum.legacy_solution_bank import newton_raphson", "", "print(newton_raphson(lambda x: x * x - 2, lambda x: 2 * x, 1.5))"),
        code("from curriculum.legacy_solution_bank import newton_raphson_recursive", "", "print(newton_raphson_recursive(lambda x: x * x - 2, lambda x: 2 * x, 1.5))"),
        code("from curriculum.legacy_solution_bank import bisection_search, newton_raphson", "", "fn = lambda x: x ** 3 - x - 2", "print(bisection_search(fn, 1, 2))", "print(newton_raphson(fn, lambda x: 3 * x * x - 1, 1.5))"),
    ],
    "10_single_variable_gd.ipynb": [
        code("from curriculum.legacy_solution_bank import exact_derivative_quadratic", "", "print(exact_derivative_quadratic(1, 2, 1, 3))"),
        code("from curriculum.legacy_solution_bank import gradient_descent_step", "", "print(gradient_descent_step(3.0, 8.0, 0.1))"),
        code("from curriculum.legacy_solution_bank import gradient_descent", "", "print(gradient_descent(lambda x: 2 * x + 2, 5.0, alpha=0.1))"),
        code("from curriculum.legacy_solution_bank import minimize_via_bisection", "", "print(minimize_via_bisection(lambda x: 2 * x + 2, -10, 10))"),
        code("from curriculum.legacy_solution_bank import gradient_descent", "", "starts = [-10, -2, 2, 10]", "results = [gradient_descent(lambda x: 4 * x ** 3 + 3 * x ** 2 - 4 * x, s, alpha=0.01) for s in starts]", "print(results)"),
    ],
    "11_multivariable_gd.ipynb": [
        code("from curriculum.legacy_solution_bank import dot_product", "", "print(dot_product([1, 2, 3], [4, 5, 6]))"),
        code("from curriculum.legacy_solution_bank import partial_derivative", "", "fn = lambda p: p[0] ** 2 + p[1] ** 2", "print(partial_derivative(fn, [3.0, 4.0], 0))"),
        code("from curriculum.legacy_solution_bank import gradient", "", "fn = lambda p: p[0] ** 2 + p[1] ** 2", "print(gradient(fn, [3.0, 4.0]))"),
        code("from curriculum.legacy_solution_bank import multivariable_gd", "", "fn = lambda p: (p[0] - 1) ** 2 + (p[1] + 2) ** 2", "print(multivariable_gd(fn, [8.0, -8.0]))"),
        code("from curriculum.legacy_solution_bank import global_minimum_search", "", "fn = lambda p: (p[0] - 1) ** 2 + (p[1] + 2) ** 2", "starts = [[5, 5], [-5, -5], [10, -10]]", "print(global_minimum_search(fn, starts))"),
        code("from curriculum.legacy_solution_bank import gradient, multivariable_gd", "", "fn = lambda p: p[0] ** 2 + 2 * p[1] ** 2", "print(gradient(fn, [2.0, 3.0]))", "print(multivariable_gd(fn, [2.0, 3.0]))"),
    ],
    "12_basic_sorting.ipynb": [
        code("from curriculum.legacy_solution_bank import selection_sort", "", "print(selection_sort([5, 2, 4, 1]))"),
        code("from curriculum.legacy_solution_bank import bubble_sort", "", "print(bubble_sort([5, 2, 4, 1]))"),
        code("from curriculum.legacy_solution_bank import insertion_sort", "", "print(insertion_sort([5, 2, 4, 1]))"),
        code("from curriculum.legacy_solution_bank import counting_sort", "", "print(counting_sort([5, 2, 4, 1, 2]))"),
        code("from curriculum.legacy_solution_bank import sort_simulated_data", "", "print(sort_simulated_data(12))"),
        code("from curriculum.legacy_solution_bank import selection_sort, bubble_sort, insertion_sort, counting_sort", "", "data = [9, 1, 8, 2, 7, 3]", "print(selection_sort(data))", "print(bubble_sort(data))", "print(insertion_sort(data))", "print(counting_sort(data))"),
    ],
    "13_advanced_sorting.ipynb": [
        code("from curriculum.legacy_solution_bank import merge", "", "print(merge([1, 4, 7], [2, 3, 6]))"),
        code("from curriculum.legacy_solution_bank import merge_sort", "", "print(merge_sort([5, 2, 4, 1]))"),
        code("from curriculum.legacy_solution_bank import partition", "", "print(partition([5, 2, 4, 1]))"),
        code("from curriculum.legacy_solution_bank import quicksort", "", "print(quicksort([5, 2, 4, 1]))"),
        code("from curriculum.legacy_solution_bank import binary_search", "", "print(binary_search([1, 2, 3, 4, 5], 4))"),
        code("from curriculum.legacy_solution_bank import merge_sort, quicksort", "", "data = [12, 4, 9, 1, 7, 3]", "print(merge_sort(data))", "print(quicksort(data))"),
    ],
    "14_basic_matrix_arithmetic.ipynb": [
        code("from curriculum.legacy_solution_bank import vector_norm, dot_product", "", "print(vector_norm([3, 4]))", "print(dot_product([1, 2], [3, 4]))"),
        code("from curriculum.legacy_solution_bank import matrix_add", "", "print(matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]]))"),
        code("from curriculum.legacy_solution_bank import matrix_multiply", "", "print(matrix_multiply([[1, 2], [3, 4]], [[2, 0], [1, 2]]))"),
        code("from curriculum.legacy_solution_bank import determinant", "", "print(determinant([[1, 2], [3, 4]]))"),
        code("from curriculum.legacy_solution_bank import determinant, matrix_multiply", "", "A = [[1, 2], [3, 4]]", "B = [[2, 0], [1, 2]]", "print(matrix_multiply(A, B))", "print(determinant(A))"),
    ],
    "15_reduced_row_echelon_form.ipynb": [
        code("from curriculum.legacy_solution_bank import eliminate_variable", "", "print(eliminate_variable([2, 1, 5], [1, -1, 1], 0))"),
        code("from curriculum.legacy_solution_bank import swap_rows, scale_row", "", "print(swap_rows([[1, 2], [3, 4]], 0, 1))", "print(scale_row([1, 2, 3], 0.5))"),
        code("from curriculum.legacy_solution_bank import rref", "", "print(rref([[1, 2], [3, 4]]))"),
        code("from curriculum.legacy_solution_bank import inverse", "", "print(inverse([[1, 2], [3, 4]]))"),
        code("from curriculum.legacy_solution_bank import rref, inverse", "", "A = [[2, 1], [5, 3]]", "print(rref(A))", "print(inverse(A))"),
    ],
    "16_k_means_clustering.ipynb": [
        code("from curriculum.legacy_solution_bank import distance", "", "print(distance([0, 0], [3, 4]))"),
        code("from curriculum.legacy_solution_bank import assign_clusters", "", "points = [[0, 0], [1, 1], [9, 9]]", "centroids = [[0, 0], [10, 10]]", "print(assign_clusters(points, centroids))"),
        code("from curriculum.legacy_solution_bank import k_means", "", "points = [[0, 0], [1, 1], [9, 9], [10, 10]]", "print(k_means(points, 2, iters=10))"),
        code("from curriculum.legacy_solution_bank import k_means", "", "points = [[0, 0], [1, 1], [9, 9], [10, 10], [8, 9]]", "for k in [1, 2, 3]:", "    print(k, k_means(points, k, iters=10)[0])"),
    ],
    "17_tic_tac_toe_connect_four.ipynb": [
        code("from curriculum.legacy_solution_bank import TicTacToe", "", "game = TicTacToe()", "game.make_move(0)", "game.make_move(4)", "print(game.display())"),
        code("from curriculum.legacy_solution_bank import ConnectFour", "", "game = ConnectFour()", "for move in [0, 1, 0, 1, 0, 1, 0]:", "    game.make_move(move)", "print(game.display())", "print(game.winner())"),
        code("from curriculum.legacy_solution_bank import TicTacToe, random_game_loop", "", "print(random_game_loop(TicTacToe()))"),
        code("from curriculum.legacy_solution_bank import TicTacToe, random_game_loop", "", "results = [random_game_loop(TicTacToe())['winner'] for _ in range(25)]", "print(results)"),
    ],
    "18_euler_estimation.ipynb": [
        code("from curriculum.legacy_solution_bank import instantaneous_rate_of_change", "", "print(instantaneous_rate_of_change(lambda t: t ** 2, 3.0))"),
        code("from curriculum.legacy_solution_bank import euler_estimation", "", "print(euler_estimation(lambda x, y: y, 0.0, 1.0, 0.1, 5))"),
        code("from curriculum.legacy_solution_bank import multivariable_euler", "", "system = lambda t, state: [state[1], -state[0]]", "print(multivariable_euler(system, 0.0, [1.0, 0.0], 0.1, 5))"),
        code("from curriculum.legacy_solution_bank import euler_estimation", "", "print(euler_estimation(lambda x, y: x + y, 0.0, 1.0, 0.1, 10))"),
    ],
    "19_sir_model.ipynb": [
        code("from curriculum.legacy_solution_bank import dS_dt, dI_dt, dR_dt", "", "print(dS_dt(999, 1, 0.2, 1000))", "print(dI_dt(999, 1, 0.2, 0.05, 1000))", "print(dR_dt(1, 0.05))"),
        code("from curriculum.legacy_solution_bank import simulate_sir", "", "print(simulate_sir(999, 1, 0, 0.2, 0.05, 0.1, 5))"),
        code("from curriculum.legacy_solution_bank import optimize_sir_params", "", "candidates = [(0.1, 0.05), (0.2, 0.05), (0.3, 0.1)]", "print(optimize_sir_params(200, candidates))"),
        code("from curriculum.legacy_solution_bank import simulate_sir", "", "history = simulate_sir(999, 1, 0, 0.25, 0.08, 0.1, 80)", "print(max(I for _, I, _ in history))"),
    ],
    "20_hodgkin_huxley.ipynb": [
        code("from curriculum.legacy_solution_bank import I_Na, I_K", "", "print(I_Na(20, 0.5, 0.6))", "print(I_K(20, 0.3))"),
        code("from curriculum.legacy_solution_bank import simulate_neuron", "", "trace = simulate_neuron(T=1.0, dt=0.01, stimulus=8.0)", "print(trace[:10])"),
        code("from curriculum.legacy_solution_bank import simulate_neuron", "", "trace = simulate_neuron(T=5.0, dt=0.01, stimulus=10.0)", "print(min(trace), max(trace))"),
    ],
    "21_hash_tables.ipynb": [
        code("from curriculum.legacy_solution_bank import hash_string", "", "print(hash_string('cat', 8))"),
        code("from curriculum.legacy_solution_bank import HashTable", "", "table = HashTable()", "table.set('cat', 3)", "table.set('dog', 5)", "print(table.get('cat'))", "print(table.items())"),
        code("from curriculum.legacy_solution_bank import count_characters_hashed", "", "table = count_characters_hashed('banana')", "print(table.items())"),
        code("from curriculum.legacy_solution_bank import HashTable", "", "table = HashTable(4)", "for key in ['aa', 'bb', 'cc', 'dd']:", "    table.set(key, len(key))", "print(table.items())"),
    ],
    "22_simplex_method.ipynb": [
        code("from curriculum.legacy_solution_bank import satisfies_inequalities", "", "constraints = [([1, 1], 4), ([2, 1], 5)]", "print(satisfies_inequalities([1, 2], constraints))"),
        code("from curriculum.legacy_solution_bank import add_slack_variables", "", "constraints = [([1, 1], 4), ([2, 1], 5)]", "print(add_slack_variables(constraints))"),
        code("from curriculum.legacy_solution_bank import simplex_pivot", "", "tableau = [[1.0, 1.0, 1.0, 0.0, 4.0], [2.0, 1.0, 0.0, 1.0, 5.0], [-3.0, -2.0, 0.0, 0.0, 0.0]]", "print(simplex_pivot(tableau, 0, 0))"),
        code("from curriculum.legacy_solution_bank import simplex_method", "", "objective = [3, 2]", "constraints = [([1, 1], 4), ([2, 1], 5)]", "print(simplex_method(objective, constraints))"),
        code("from curriculum.legacy_solution_bank import simplex_method", "", "print(simplex_method([5, 4], [([6, 4], 24), ([1, 2], 6), ([-1, 1], 1)]))"),
    ],
    "23-25_regression_pseudoinverse.ipynb": [
        code("from curriculum.legacy_solution_bank import pseudoinverse", "", "print(pseudoinverse([[1, 0], [1, 1], [1, 2]]))"),
        code("from curriculum.legacy_solution_bank import polynomial_regression", "", "print(polynomial_regression([0, 1, 2], [1, 3, 7], 2))"),
        code("from curriculum.legacy_solution_bank import transform_exponential, transform_logistic", "", "print(transform_exponential([0, 1, 2], [2, 4, 8]))", "print(transform_logistic([0, 1, 2, 3], [0.1, 0.25, 0.65, 0.85]))"),
        code("from curriculum.legacy_solution_bank import nonlinear_regression", "", "print(nonlinear_regression([0, 1, 2], [1, 3, 7], model='polynomial', degree=2))"),
        code("from curriculum.legacy_solution_bank import polynomial_regression, transform_exponential, transform_logistic", "", "print(polynomial_regression([0, 1, 2, 3], [1, 2, 5, 10], 2))", "print(transform_exponential([0, 1, 2], [2, 4, 8]))", "print(transform_logistic([0, 1, 2, 3], [0.1, 0.25, 0.65, 0.85]))"),
    ],
    "26_overfitting_bias_variance.ipynb": [
        code("from curriculum.legacy_solution_bank import train_test_split", "", "X = list(range(10))", "y = [x * x for x in X]", "print(train_test_split(X, y, test_ratio=0.3, seed=0))"),
        code("from curriculum.legacy_solution_bank import k_fold_cross_validation", "", "model_fn = lambda X_train, y_train: (lambda x: x)", "print(k_fold_cross_validation(model_fn, [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], k=5))"),
        code("from curriculum.legacy_solution_bank import compute_mse", "", "print(compute_mse([1, 2, 3], [1, 2, 4]))"),
        code("from curriculum.legacy_solution_bank import compute_mse", "", "degrees = {1: [1, 2, 3], 3: [1, 2, 3.1], 8: [1, 2, 8]}", "for degree, preds in degrees.items():", "    print(degree, compute_mse([1, 2, 3], preds))"),
    ],
    "27-28_regression_gradient_descent.ipynb": [
        code("from curriculum.legacy_solution_bank import mse_gradient", "", "print(mse_gradient([[1, 1], [1, 2]], [2, 3], [0, 0]))"),
        code("from curriculum.legacy_solution_bank import multiple_regression_gd", "", "X = [[1, 1], [1, 2], [1, 3]]", "y = [2, 3, 4]", "print(multiple_regression_gd(X, y, alpha=0.1, epochs=500))"),
        code("from curriculum.legacy_solution_bank import add_interaction_terms", "", "print(add_interaction_terms([[2, 3], [4, 5]]))"),
        code("from curriculum.legacy_solution_bank import optimize_weights_gd", "", "X = [[1, 1], [1, 2], [1, 3]]", "y = [2, 3, 4]", "print(optimize_weights_gd(X, y, [0.01, 0.05, 0.1], epochs=500))"),
        code("from curriculum.legacy_solution_bank import add_interaction_terms, multiple_regression_gd", "", "X = add_interaction_terms([[1, 2], [2, 3], [3, 4]])", "y = [5, 9, 15]", "print(multiple_regression_gd(X, y, alpha=0.01, epochs=1000))"),
    ],
    "29_k_nearest_neighbors.ipynb": [
        code("from curriculum.legacy_solution_bank import get_neighbors", "", "X = [[0, 0], [1, 1], [10, 10]]", "y = ['A', 'A', 'B']", "print(get_neighbors(X, y, [0.5, 0.5], 2))"),
        code("from curriculum.legacy_solution_bank import knn_classify", "", "X = [[0, 0], [1, 1], [10, 10]]", "y = ['A', 'A', 'B']", "print(knn_classify(X, y, [0.5, 0.5], 2))"),
        code("from curriculum.legacy_solution_bank import knn_classify", "", "dataset = [[0, 0], [1, 1], [0, 1], [8, 8], [9, 9]]", "labels = ['A', 'A', 'A', 'B', 'B']", "for k in [1, 3]:", "    print(k, knn_classify(dataset, labels, [0.8, 0.7], k))"),
    ],
    "30_naive_bayes.ipynb": [
        code("from curriculum.legacy_solution_bank import compute_probabilities", "", "rows = [['win', 'money'], ['project', 'meeting'], ['win', 'prize']]", "labels = ['spam', 'ham', 'spam']", "print(compute_probabilities(rows, labels))"),
        code("from curriculum.legacy_solution_bank import naive_bayes_classify", "", "rows = [['win', 'money'], ['project', 'meeting'], ['win', 'prize']]", "labels = ['spam', 'ham', 'spam']", "print(naive_bayes_classify(rows, labels, ['win', 'money']))"),
        code("from curriculum.legacy_solution_bank import naive_bayes_classify", "", "rows = [['cheap', 'pills'], ['team', 'meeting'], ['cheap', 'offer']]", "labels = ['spam', 'ham', 'spam']", "print(naive_bayes_classify(rows, labels, ['cheap', 'offer']))"),
    ],
    "31_bfs_dfs.ipynb": [
        code("from curriculum.legacy_solution_bank import bfs", "", "graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}", "print(bfs(graph, 'A'))"),
        code("from curriculum.legacy_solution_bank import dfs_iterative, dfs_recursive", "", "graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}", "print(dfs_iterative(graph, 'A'))", "print(dfs_recursive(graph, 'A'))"),
        code("from curriculum.legacy_solution_bank import find_connected_components", "", "graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}", "print(find_connected_components(graph))"),
        code("from curriculum.legacy_solution_bank import bfs, dfs_iterative", "", "graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}", "print(bfs(graph, 'A'))", "print(dfs_iterative(graph, 'A'))"),
    ],
    "32-33_shortest_paths_dijkstra.ipynb": [
        code("from curriculum.legacy_solution_bank import PriorityQueue", "", "pq = PriorityQueue()", "pq.push(2, 'B')", "pq.push(1, 'A')", "print(pq.pop())", "print(pq.pop())"),
        code("from curriculum.legacy_solution_bank import dijkstra", "", "graph = {'A': [('B', 1), ('C', 4)], 'B': [('C', 2), ('D', 5)], 'C': [('D', 1)], 'D': []}", "print(dijkstra(graph, 'A'))"),
        code("from curriculum.legacy_solution_bank import unweighted_shortest_path_bfs", "", "graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}", "print(unweighted_shortest_path_bfs(graph, 'A'))"),
        code("from curriculum.legacy_solution_bank import dijkstra, unweighted_shortest_path_bfs", "", "weighted = {'A': [('B', 1), ('C', 1)], 'B': [('D', 1)], 'C': [('D', 1)], 'D': []}", "unweighted = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}", "print(dijkstra(weighted, 'A')[0])", "print(unweighted_shortest_path_bfs(unweighted, 'A'))"),
    ],
    "34_decision_trees.ipynb": [
        code("from curriculum.legacy_solution_bank import safe_p_log_p", "", "print(safe_p_log_p(0.5))"),
        code("from curriculum.legacy_solution_bank import calculate_entropy, information_gain", "", "print(calculate_entropy(['yes', 'yes', 'no', 'no']))", "rows = [{'Weather': 'Sunny', 'Play': 'No'}, {'Weather': 'Rainy', 'Play': 'Yes'}, {'Weather': 'Sunny', 'Play': 'No'}]", "print(information_gain(rows, 'Weather', 'Play'))"),
        code("from curriculum.legacy_solution_bank import build_decision_tree", "", "rows = [{'Weather': 'Sunny', 'Windy': 'No', 'Play': 'No'}, {'Weather': 'Rainy', 'Windy': 'No', 'Play': 'Yes'}, {'Weather': 'Rainy', 'Windy': 'Yes', 'Play': 'No'}]", "print(build_decision_tree(rows, 'Play'))"),
        code("from curriculum.legacy_solution_bank import build_decision_tree, print_tree_dfs", "", "rows = [{'Weather': 'Sunny', 'Windy': 'No', 'Play': 'No'}, {'Weather': 'Rainy', 'Windy': 'No', 'Play': 'Yes'}, {'Weather': 'Rainy', 'Windy': 'Yes', 'Play': 'No'}]", "tree = build_decision_tree(rows, 'Play')", "print_tree_dfs(tree)"),
        code("from curriculum.legacy_solution_bank import calculate_entropy", "", "labels = ['cat', 'cat', 'dog', 'dog', 'dog']", "print(calculate_entropy(labels))"),
    ],
    "35-36_neural_networks.ipynb": [
        code("from curriculum.legacy_solution_bank import chain_rule_gradient", "", "print(chain_rule_gradient(3, 4))"),
        code("from curriculum.legacy_solution_bank import forward_pass", "", "weights = [[[0.5, -0.25], [0.3, 0.8]], [[0.4], [-0.7]]]", "biases = [[0.0, 0.0], [0.1]]", "print(forward_pass([1.0, 0.5], weights, biases))"),
        code("from curriculum.legacy_solution_bank import backpropagation", "", "weights = [[[0.5, -0.25], [0.3, 0.8]], [[0.4], [-0.7]]]", "biases = [[0.0, 0.0], [0.1]]", "print(backpropagation([1.0, 0.5], None, [1.0], weights, biases))"),
        code("from curriculum.legacy_solution_bank import train_network", "", "X = [[0, 0], [0, 1], [1, 0], [1, 1]]", "Y = [0, 1, 1, 0]", "print(train_network(X, Y, epochs=50, alpha=0.1))"),
        code("from curriculum.legacy_solution_bank import train_network, forward_pass", "", "X = [[0, 0], [0, 1], [1, 0], [1, 1]]", "Y = [0, 1, 1, 0]", "weights, biases = train_network(X, Y, epochs=50, alpha=0.1)", "print([forward_pass(x, weights, biases)[-1].tolist() for x in X])"),
    ],
    "37-39_minimax_game_trees.ipynb": [
        code("from curriculum.legacy_solution_bank import minimax", "", "moves = lambda state: state", "apply_move = lambda state, move, player: []", "terminal = lambda state: (True, 1 if state == [] else 0)", "print(minimax([], 1, lambda s: [], terminal, lambda s: 0))"),
        code("from curriculum.legacy_solution_bank import alphabeta", "", "children = lambda state: state", "terminal = lambda state: (len(state) == 0, 0)", "evaluate = lambda state: len(state)", "print(alphabeta([[[]], []], 2, -999, 999, True, children, terminal, evaluate))"),
        code("from curriculum.legacy_solution_bank import evaluate_connect_four", "", "board = [[' '] * 7 for _ in range(6)]", "board[5][3] = 'X'", "board[4][3] = 'X'", "print(evaluate_connect_four(board, 'X'))"),
        code("from curriculum.legacy_solution_bank import evaluate_connect_four", "", "board = [[' '] * 7 for _ in range(6)]", "for r in [5, 4, 3]:", "    board[r][3] = 'X'", "print(evaluate_connect_four(board))"),
    ],
    "40-42_neuroevolution.ipynb": [
        code("from curriculum.legacy_solution_bank import evaluate_relative_fitness", "", "import numpy as np", "population = [np.array([1, 2, 3]), np.array([3, 2, 1])]", "print(evaluate_relative_fitness(population, lambda w: np.sum(w)))"),
        code("from curriculum.legacy_solution_bank import evaluate_board_mlp", "", "import numpy as np", "print(evaluate_board_mlp([1, 0, -1], np.array([0.3, 0.2, -0.5])))"),
        code("from curriculum.legacy_solution_bank import evolve_population_tournament", "", "import numpy as np", "population = [np.array([1.0, 2.0]), np.array([0.5, 0.5]), np.array([3.0, 1.0]), np.array([2.0, 2.0])]", "print(evolve_population_tournament(population, lambda w: float(np.sum(w)), generations=2))"),
        code("from curriculum.legacy_solution_bank import train_blondie24_agent", "", "print(train_blondie24_agent(board_size=9, population_size=6, generations=2))"),
        code("from curriculum.legacy_solution_bank import train_blondie24_agent", "", "agent = train_blondie24_agent(board_size=9, population_size=6, generations=3)", "print(agent.shape if hasattr(agent, 'shape') else len(agent))"),
    ],
    "43_convolutional_blondie24.ipynb": [
        code("from curriculum.legacy_solution_bank import apply_convolution_2d", "", "board = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]", "kernel = [[1, 0], [0, -1]]", "print(apply_convolution_2d(board, kernel))"),
        code("from curriculum.legacy_solution_bank import max_pooling_2d", "", "print(max_pooling_2d([[1, 2], [3, 4]]))"),
        code("from curriculum.legacy_solution_bank import evaluate_board_cnn", "", "board = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]", "kernel = [[1, 0], [0, -1]]", "print(evaluate_board_cnn(board, kernel, [0.5, -0.25, 0.1, 0.2]))"),
        code("from curriculum.legacy_solution_bank import train_convolutional_blondie24", "", "print(train_convolutional_blondie24(board_shape=(6, 7), generations=2))"),
        code("from curriculum.legacy_solution_bank import train_convolutional_blondie24", "", "model = train_convolutional_blondie24(board_shape=(6, 7), generations=3)", "print(model.keys())"),
    ],
    "math_01_algebra_linear_equations.ipynb": [
        code("from curriculum.legacy_solution_bank import solve_linear", "", "print(solve_linear(3, -4, 11))"),
        code("from curriculum.legacy_solution_bank import solve_complex_linear", "", "print(solve_complex_linear(3, 2, 11, d=-4))"),
        code("from curriculum.legacy_solution_bank import verify_solution", "", "print(verify_solution(3, -4, 11, 5))"),
        code("from curriculum.legacy_solution_bank import solve_linear, verify_solution", "", "x = solve_linear(5, -7, 18)", "print(x, verify_solution(5, -7, 18, x))"),
    ],
    "math_02_calculus_derivatives.ipynb": [
        code("from curriculum.legacy_solution_bank import difference_quotient", "", "print(difference_quotient(lambda x: x ** 2, 3, 0.001))"),
        code("from curriculum.legacy_solution_bank import exact_derivative", "", "print(exact_derivative([4, -1, 7]))"),
        code("from curriculum.legacy_solution_bank import difference_quotient, exact_derivative", "", "print(difference_quotient(lambda x: 7 * x ** 2 - x + 4, 2, 1e-5))", "print(exact_derivative([4, -1, 7]))"),
    ],
    "math_03_calculus_chain_rule.ipynb": [
        code("from curriculum.legacy_solution_bank import inner_g_prime, outer_f_prime", "", "print(inner_g_prime(3))", "print(outer_f_prime(4))"),
        code("from curriculum.legacy_solution_bank import chain_rule", "", "print(chain_rule(3))"),
        code("from curriculum.legacy_solution_bank import chain_rule", "", "print(chain_rule(1.5))"),
    ],
    "math_04_calculus_local_extrema.ipynb": [
        code("from curriculum.legacy_solution_bank import find_minimum_vertex", "", "print(find_minimum_vertex(1, -4, 7))"),
        code("from curriculum.legacy_solution_bank import bisection_root_finding", "", "print(bisection_root_finding(lambda x: 2 * x - 4, 0, 5))"),
        code("from curriculum.legacy_solution_bank import find_minimum_vertex", "", "print(find_minimum_vertex(2, -8, 1))"),
    ],
    "math_05_linear_algebra_vectors.ipynb": [
        code("from curriculum.legacy_solution_bank import vector_add, vector_norm", "", "print(vector_add([1, 2], [3, 4]))", "print(vector_norm([3, 4]))"),
        code("from curriculum.legacy_solution_bank import dot_product", "", "print(dot_product([1, 2, 3], [4, 5, 6]))"),
        code("from curriculum.legacy_solution_bank import vector_angle", "", "print(vector_angle([1, 0], [0, 1]))"),
        code("from curriculum.legacy_solution_bank import vector_add, vector_angle", "", "print(vector_add([2, 1], [-1, 3]))", "print(vector_angle([1, 1], [1, 0]))"),
    ],
    "math_06_linear_algebra_matrices.ipynb": [
        code("from curriculum.legacy_solution_bank import matrix_vector_mult", "", "print(matrix_vector_mult([[1, 2], [3, 4]], [5, 6]))"),
        code("from curriculum.legacy_solution_bank import matrix_mult", "", "print(matrix_mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))"),
        code("from curriculum.legacy_solution_bank import matrix_mult", "", "A = [[1, 1], [0, 1]]", "print(matrix_mult(A, A))"),
    ],
    "math_07_calculus_differential_equations.ipynb": [
        code("from curriculum.legacy_solution_bank import euler_population", "", "print(euler_population(100, 0.05, 0.1, 5))"),
        code("from curriculum.legacy_solution_bank import euler_population", "", "print(euler_population(50, 0.08, 0.05, 20))"),
    ],
}


def replace_placeholder_cells(path: Path, replacements: list[str]) -> None:
    nb = json.loads(path.read_text(encoding="utf-8"))
    cells = nb.get("cells", [])
    placeholder_indices = [i for i, cell in enumerate(cells) if PLACEHOLDER in "\n".join(cell.get("source", []))]
    if not placeholder_indices:
        print(f"already complete {path.relative_to(ROOT)}")
        return
    if len(placeholder_indices) != len(replacements):
        raise ValueError(f"{path.name}: expected {len(replacements)} placeholders, found {len(placeholder_indices)}")
    for index, replacement in zip(placeholder_indices, replacements):
        cells[index]["source"] = replacement.split("\n")
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"completed {path.relative_to(ROOT)}")


def main() -> int:
    for name, replacements in REPLACEMENTS.items():
        replace_placeholder_cells(SOLUTIONS / name, replacements)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
