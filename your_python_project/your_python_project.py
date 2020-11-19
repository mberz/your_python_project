"""Main module."""

import numpy as np


def say_hello(name='World'):
    """Say hello to someone

    Parameters
    ----------
    name : string
        A string containing the name of the person who is to greeted.

    Returns
    -------
    string : string
        The greetings string.

    """
    if not isinstance(name, str):
        raise ValueError("I need a string.")
    string = 'Hello {}!'.format(name)
    return string


def giva_me_a_range():
    return np.arange(1, 10) + 1e-10


def return_sine():
    times = np.arange(0, 2*np.pi)
    return np.sin(times)
