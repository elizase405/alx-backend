#!/usr/bin/env python3
"""
    A module with 1 function: index_range(3, 15) - (30, 45)
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
