#!/usr/bin/env python3
"""Module having an async_generator coroutine that yields random values
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Method is a coroutine  that yields 10 random numbers between 0 and 20
       asynchronously. Each yield is preceded by a 1-second wait.

       Returns:
           An async generator that yields random floats
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
