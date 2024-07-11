#!/usr/bin/env python3
import csv
import math
from typing import List

"""
    A module with 1 function and 1 class:
        index_range(3, 15) - (30, 45)
        Server().get_page(3, 15) - returns a list of 15 lists
            containing the content from index 29
            to 44(list are 0 indexed so we start at 29 not 30)
"""


def index_range(page, page_size):
    """
        Calculate the start index and end index of a particular page

        Args:
            page (int) page no we currently want
            page_size (int) no of items on the page
        Return:
            A tuple of size two containing a
            start index and an end index of the page
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


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
        assert isinstance(page, int) and page > 0, 'Integer must be > 0'
        assert isinstance(page_size, int) and page_size > 0, "be > 0"
        # returns the start and end index of the content in a page
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]
