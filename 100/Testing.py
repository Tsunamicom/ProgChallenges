import unittest
import p100


class Test(unittest.TestCase):

    def test_num_range(self):
        self.assertListEqual(p100.num_range(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertListEqual(p100.num_range(10, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_num_seq(self):
        self.assertEquals(p100.num_seq(5), 6)
        self.assertEquals(p100.num_seq(50), 25)


if __name__ == '__main__':
    unittest.main()
