#!/usr/bin/env python3

from typing import Tuple
def index_range(page, page_size):
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start and end indices (0-indexed) for the specified page.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size should be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 0

    return start_index, end_index
