#!/usr/bin/env python3
""" Task 1 """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters"""
    return tuple(map(lambda x: x * page_size, [page-1, page]))
