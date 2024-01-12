#!/usr/bin/env python3
""" Defines a func that return a funnc """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ a func that call another func """

    def mult(m: float) -> float:
        """ return m mutliplied by multiplier """
        return m * multiplier

    return mult
