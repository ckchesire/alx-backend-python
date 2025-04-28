#!/usr/bin/env python3
"""Module that returns an asyncio task
"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function to create and return an asyncio.Task for wait_random.

    Args:
        max_delay (int): Maximum delay time.

    Returns:
        asyncio.Task: A created asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
