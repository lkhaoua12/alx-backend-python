#!/usr/bin/env python3
""" Modle defines a function that takes a list of floats """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """func that takes a list of floats and returns their sum"""
    return sum(mxd_lst)
