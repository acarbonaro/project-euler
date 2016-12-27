import euler001, euler002, euler003, euler004, euler005, euler006
import unittest


class TestSolutions(unittest.TestCase):
    def test_euler001(self):
        self.assertEqual(233168, euler001.solution())

    def test_euler002(self):
        self.assertEqual(4613732, euler002.solution())

    def test_euler003(self):
        self.assertEqual(-1, euler003.solution())

    def test_euler004(self):
        self.assertEqual(906609, euler004.solution())

    def test_euler005(self):
        self.assertEqual(232792560, euler005.solution())

    def test_euler006(self):
        self.assertEqual(25164150, euler006.solution())


if __name__ == '__main__':
    unittest.main()
