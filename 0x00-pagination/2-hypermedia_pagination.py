#!/usr/bin/env python3
""" Task 2 """

import csv
from math import ceil
from typing import Dict, List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return the appropriate page of the dataset """
        assert (isinstance(page, int) and
                isinstance(page_size, int) and
                page > 0 and page_size > 0)
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int]:
        """return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return
        in a list for those particular pagination parameters"""
        return tuple(map(lambda x: x * page_size, [page-1, page]))

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """return a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)"""
        safe_page_size = page_size if page_size > 0 else 1
        data = self.get_page(page, safe_page_size)
        page_size = len(data)
        total_size = len(self.dataset())
        total_pages = ceil(total_size/safe_page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        return {"data": data, "page_size": page_size,
                "page": page, "prev_page": prev_page,
                "next_page": next_page, "total_pages": total_pages}
