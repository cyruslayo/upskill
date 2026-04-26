import math
import unittest

import numpy as np

from curriculum.legacy_solution_bank import (
    HashTable,
    TicTacToe,
    add_interaction_terms,
    apply_convolution_2d,
    binary_to_decimal,
    bfs,
    build_decision_tree,
    check_if_symmetric,
    count_characters_hashed,
    dijkstra,
    euler_population,
    gradient_descent,
    k_means,
    knn_classify,
    matrix_multiply,
    polynomial_regression,
    pseudoinverse,
    selection_sort,
    simplex_method,
    solve_linear,
    train_network,
)


class LegacySolutionBankTests(unittest.TestCase):
    def test_foundations(self):
        self.assertTrue(check_if_symmetric("racecar"))
        self.assertEqual(binary_to_decimal("11010"), 26)
        self.assertEqual(solve_linear(3, -4, 11), 5)

    def test_sorting_and_linear_algebra(self):
        self.assertEqual(selection_sort([5, 1, 3]), [1, 3, 5])
        self.assertEqual(matrix_multiply([[1, 2]], [[3], [4]]), [[11]])
        pinv = np.array(pseudoinverse([[1, 0], [1, 1], [1, 2]]))
        self.assertEqual(pinv.shape, (2, 3))

    def test_regression_and_gd(self):
        coeffs = polynomial_regression([0, 1, 2], [1, 3, 7], 2)
        self.assertAlmostEqual(coeffs[0], 1.0, places=5)
        minimum = gradient_descent(lambda x: 2 * x + 2, 5.0, alpha=0.1)
        self.assertAlmostEqual(minimum, -1.0, places=3)
        self.assertEqual(add_interaction_terms([[2, 3]])[0], [2, 3, 6])

    def test_graphs_and_ml(self):
        self.assertEqual(bfs({"A": ["B"], "B": []}, "A"), ["A", "B"])
        distances, _ = dijkstra({"A": [("B", 1)], "B": []}, "A")
        self.assertEqual(distances["B"], 1.0)
        label = knn_classify([[0, 0], [1, 1], [9, 9]], ["A", "A", "B"], [0.2, 0.2], 2)
        self.assertEqual(label, "A")
        centroids, labels = k_means([[0, 0], [1, 1], [9, 9], [10, 10]], 2, iters=10)
        self.assertEqual(len(centroids), 2)
        self.assertEqual(len(labels), 4)

    def test_data_structures_and_games(self):
        table = HashTable()
        table.set("cat", 3)
        self.assertEqual(table.get("cat"), 3)
        hashed = count_characters_hashed("banana")
        self.assertEqual(hashed.get("a"), 3)
        game = TicTacToe()
        game.make_move(0)
        game.make_move(3)
        game.make_move(1)
        game.make_move(4)
        game.make_move(2)
        self.assertEqual(game.winner(), "X")

    def test_advanced_algorithms(self):
        result = simplex_method([3, 2], [([1, 1], 4), ([2, 1], 5)])
        self.assertAlmostEqual(result["value"], 9.0, places=5)
        conv = apply_convolution_2d([[1, 0], [0, 1]], [[1, 0], [0, -1]])
        self.assertEqual(conv, [[0.0]])
        population = euler_population(100, 0.05, 0.1, 1)
        self.assertEqual(len(population), 2)
        weights, biases = train_network([[0, 0], [1, 1]], [0, 1], epochs=5, alpha=0.1)
        self.assertEqual(len(weights), 2)
        self.assertEqual(len(biases), 2)
        tree = build_decision_tree(
            [
                {"Weather": "Sunny", "Play": "No"},
                {"Weather": "Rainy", "Play": "Yes"},
            ],
            "Play",
        )
        self.assertTrue(tree == "No" or isinstance(tree, dict))


if __name__ == "__main__":
    unittest.main()

