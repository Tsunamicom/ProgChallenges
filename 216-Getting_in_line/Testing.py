import p216
import unittest


class Test(unittest.TestCase):
    def test_conn_length(self):
        assertTrue(p216.conn_length((1, 1), (2, 2)), 1.4142135623730951)


if __name__ == '__main__':
    unittest.main()
