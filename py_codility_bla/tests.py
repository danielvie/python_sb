import unittest
from main import solution

class TestCases(unittest.TestCase):
    
    def test_1(self):
        S = "cdeo"
        A = [3,2,0,1]
        self.assertEqual(solution(S, A), "code")

    def test_3(self):
        S = "cdeenetpi"
        A = [5,2,0,1,6,4,8,3,7]
        self.assertEqual(solution(S, A), "centipede")

    def test_2(self):
        S = "bytdag"
        A = [4,3,0,1,2,5]
        self.assertEqual(solution(S, A), "bat")


if __name__ == "__main__":
    
    unittest.main()
