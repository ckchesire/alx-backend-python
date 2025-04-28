#!/usr/bin/env python3
"""Module that defines an asynchronous coroutine to wait for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Method for asynchronously wait for a random delay between 0 and
       max_delay.

       Args:
          max_delay (int): max no. of seconds to wait. Default being 10.

       Returns:
          float: The actual delay waited before returning.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
