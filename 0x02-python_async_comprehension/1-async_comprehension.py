#!/usr/bin/env python3
"""
Module that uses collects random numbers using async comprehension
"""
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over async_generator.

    Returns:
        List[float]: A list of 10 random float numbers
    """
    return [number async for number in async_generator()]
