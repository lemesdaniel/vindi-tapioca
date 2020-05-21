# coding: utf-8

import unittest

from tapioca_vindi import Vindi


class TestTapiocaVindi(unittest.TestCase):

    def setUp(self):
        self.wrapper = Vindi()


if __name__ == '__main__':
    unittest.main()
