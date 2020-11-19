#!/usr/bin/env python

"""Tests for `your_python_project` package."""

import pytest
import numpy as np
import numpy.testing as npt


from your_python_project import your_python_project


def test_hello_world():
    expected = 'Hello World!'
    string = your_python_project.say_hello()

    assert expected == string


def test_hello_fabian():
    expected = 'Hello Fabian!'
    string = your_python_project.say_hello('Fabian')

    assert expected == string


def test_error():
    with pytest.raises(ValueError):
        your_python_project.say_hello(1)


def test_a_range():
    expected = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    actual = your_python_project.giva_me_a_range()

    npt.assert_allclose(actual, expected, rtol=1e-9)
