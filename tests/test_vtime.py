import pytest

import logging
from time import sleep

import vtime


def test_version():
    assert vtime.__version__ == "2.0.0"


def test_timeit():
    """ Test the timeit function """

    dummy_function = lambda x: x + 2

    @vtime.timeit
    def timeit_function(x):
        return dummy_function(x)

    assert dummy_function(42) == timeit_function(42)


def test_timeit_out():
    """ Test the timeit_out function """

    @vtime.timeit_out
    def sleep_1():
        return sleep(1)

    out, total_time = sleep_1()

    # Check output
    assert out is None

    # Check time (one decimal precision)
    assert pytest.approx(total_time, 1) == 1


def test_stimeit():
    """ Test the stimeit function """

    dummy_function = lambda x: x + 2

    @vtime.stimeit(logging.info)
    def stimeit_function(x):
        return dummy_function(x)

    assert dummy_function(42) == stimeit_function(42)


def test_mesure():
    """ Test the stimeit function """

    num_tests = 10
    sleep_time = 0.1

    out = vtime.mesure(sleep, sleep_time, n_iterations=num_tests)

    assert len(out) == num_tests

    # n times 1 second should be between 9 and 11
    assert (num_tests - 1) * sleep_time <= sum(out) <= (num_tests + 1) * sleep_time


def test_time_human():
    """ Test get time_human function """

    data = [
        (58, "58.00 s"),
        (90, "1.50 min"),
        (3600, "1.00 h"),
        (3600 * 24, "1.00 days"),
        (3600 * 24 * 365, "1.00 years"),
    ]

    for value, result in data:
        assert vtime.time_human(value) == result
