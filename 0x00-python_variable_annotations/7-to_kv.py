#!/usr/bin/env python3
""" module that defines a function."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Func that takes a string k and an int OR float v as arguments"""
    return (k, v**2)
