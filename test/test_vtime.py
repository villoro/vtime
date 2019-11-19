"""
    Tests for v_time.py
"""

import unittest
import logging
from time import sleep

import v_time


class TestVTime(unittest.TestCase):
    """Test v_time"""

    def test_timeit(self):
        """ Test the timeit function """

        dummy_function = lambda x: x + 2

        @v_time.timeit
        def timeit_function(x):
            return dummy_function(x)

        self.assertEqual(dummy_function(42), timeit_function(42))

    def test_stimeit(self):
        """ Test the stimeit function """

        dummy_function = lambda x: x + 2

        @v_time.stimeit(logging.info)
        def stimeit_function(x):
            return dummy_function(x)

        self.assertEqual(dummy_function(42), stimeit_function(42))

    def test_mesure(self):
        """ Test the stimeit function """

        out = v_time.mesure(sleep, 10, 1)

        self.assertEqual(len(out), 10)

        # 10 times 1 second should be between 9 and 11
        self.assertTrue(9 <= sum(out) <= 11)
