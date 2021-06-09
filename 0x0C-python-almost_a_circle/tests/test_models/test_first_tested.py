#!/usr/bin/python3

import unittest

class TestFirst(unittest.TestCase):
    def test_es_mayor_que(self):
        self.assertTrue(15 >7)

if __name__=="__main__":
    unittest.main()
