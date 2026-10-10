"""Unit tests for the sample application."""

import unittest

from app import add, greet


class TestApp(unittest.TestCase):
    def test_greet_name(self):
        self.assertEqual(greet("Riya"), "Hello, Riya!")

    def test_greet_empty_name(self):
        self.assertEqual(greet(""), "Hello, World!")

    def test_greet_strips_spaces(self):
        self.assertEqual(greet("  Riya  "), "Hello, Riya!")

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, 1), -1)


if __name__ == "__main__":
    unittest.main()
