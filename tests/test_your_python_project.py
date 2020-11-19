#!/usr/bin/env python

"""Tests for `your_python_project` package."""

import pytest


from your_python_project import your_python_project


def test_hello_world():
    expected = 'Hello World!'
    string = your_python_project.say_hello()

    assert expected == string


def test_hello_fabian():
    expected = 'Hello Fabian!'
    string = your_python_project.say_hello('Fabian')

    assert expected == string
