import unittest
from app import n_queen

class TestNQueen(unittest.TestCase):
    
    def test_n_queen(self):
        # Test the function with different values of n and first queen positions
        test_cases = [
            (4, None, [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]),
            (8, None, [
                [1, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 1, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 1], 
                [0, 0, 0, 0, 0, 1, 0, 0], 
                [0, 0, 1, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 1, 0], 
                [0, 1, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 1, 0, 0, 0, 0]
            ]),
            (8, [0, 3], [
                [0, 0, 0, 1, 0, 0, 0, 0], 
                [1, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 1, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 1], 
                [0, 1, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 1, 0], 
                [0, 0, 1, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 1, 0, 0]
            ])
        ]
        for n, first_queen, expected in test_cases:
            with self.subTest(n=n, first_queen=first_queen):
                self.assertEqual(n_queen(n, first_queen), expected)

if __name__ == '__main__':
    unittest.main()