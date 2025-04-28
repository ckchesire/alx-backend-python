#!/usr/bin/env python3
"""Module to calculate runtime for wait_n
"""

import time
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function to calculate the average of wait_n

       Args:
           n (int): Number of times wait_random is called
           max_delay (int): max delay for each wait_random

       Returns:
           float : Average time per wait_random call.
    """
    start_time = time.time()
    import asyncio
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
