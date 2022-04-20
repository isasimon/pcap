import unittest


class TestOps(unittest.TestCase):
    def test_expo(self):
        self.assertEqual(2 ** 3, 8)


if __name__ == '__main__':
    unittest.main()
