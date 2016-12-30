import euler001, euler002, euler003, euler004, euler005, euler006, euler007,\
    euler008, euler009, euler010, euler011
import unittest


class TestSolutions(unittest.TestCase):
    def test_euler001(self):
        self.assertEqual(23, euler001.test())
        self.assertEqual(233168, euler001.solution())

    def test_euler002(self):
        self.assertEqual(10, euler002.test())
        self.assertEqual(4613732, euler002.solution())

    def test_euler003(self):
        self.assertEqual(29, euler003.test())

    def test_euler004(self):
        self.assertEqual(9009, euler004.test())
        self.assertEqual(906609, euler004.solution())

    def test_euler005(self):
        self.assertEqual(2520, euler005.test())
        self.assertEqual(232792560, euler005.solution())

    def test_euler006(self):
        self.assertEqual(2640, euler006.test())
        self.assertEqual(25164150, euler006.solution())

    def test_euler007(self):
        self.assertEqual(13, euler007.test())
        self.assertEqual(104743, euler007.solution())

    def test_euler008(self):
        self.assertEqual(5832, euler008.test())
        self.assertEqual(23514624000, euler008.solution())

    def test_euler009(self):
        self.assertEqual(60, euler009.test())
        self.assertEqual(31875000, euler009.solution())

    def test_euler010(self):
        self.assertEqual(17, euler010.test())
        self.assertEqual(142913828922, euler010.solution())

    def test_euler011(self):
        self.assertEqual(1788696, euler011.test())
        self.assertEqual(70600674, euler011.solution())


if __name__ == '__main__':
    unittest.main()
