#!/usr/bin/env python3
""" this module define a func that take a Sequence """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes a Sequence and return a list of tuples.
    """
    return [(i, len(i)) for i in lst]
