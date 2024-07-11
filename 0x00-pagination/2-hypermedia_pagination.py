#!/usr/bin/env python3
"""
    A module with 1 function and 1 class:
        index_range(3, 15) - (30, 45)
        Server().get_hyper(3, 15) - returns a dictionary
"""

import csv
import math
from typing import Dict, List
import math


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
        """
            get content of certain page
            Args:
                page (int) page no we currently want
                page_size (int) no of items on the page
        Return:
            A list of lists containing the content of the given page
        """

        assert isinstance(page, int) and page > 0, 'Integer must be > 0'
        assert isinstance(page_size, int) and page_size > 0, "be > 0"
        # returns the start and end index of the content in a page
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            get contents and details of certain page
            Args:
                page (int) page no we currently want
                page_size (int) no of items on the page
        Return:
            A dictionary containing information of the given page
        """

        data = self.get_page(page, page_size)
        next_page = page + 1
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        dataset = self.dataset()
        if data == []:
            total_pages = math.ceil(len(dataset) / page_size)
        else:
            total_pages = math.floor(len(dataset) / page_size)
        if total_pages < page:
            page_size = 0
            next_page = None
        details = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
            }
        return details
