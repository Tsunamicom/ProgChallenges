import p216
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.networks = [[(1, 1), (2, 3), (15, 20)], [(32, 42), (12, 4), (14, 12), (150, 0)]]
        self.master = dict()
        self.network_list = list()


    def test_network_distances(self):
        self.assertTrue(p216.network_distances,
                        self.network_list ==
                        [
                            [
                                [(1, 1), (2, 3), 2.23606797749979],
                                [(2, 3), (15, 20), 21.400934559032695]
                            ],
                            [
                                [(12, 4), (14, 12), 8.246211251235321],
                                [(14, 12),(32, 42), 34.9857113690718],
                                [(32, 42), (150, 0), 125.25174649480941]
                            ]
                        ]
                       )


    def test_con_length(self):
        self.assertEqual(p216.con_length(((1, 1), (2, 2))), 1.4142135623730951)
        self.assertEqual(p216.con_length(((15, 25), (12, 16))), 9.486832980505138)
        self.assertEqual(p216.con_length(((0, 150), (13, 6))), 144.5856147754679)


    def tearDown(self):
       del self.networks
       del self.master
       del self.network_list


if __name__ == '__main__':
    unittest.main()
