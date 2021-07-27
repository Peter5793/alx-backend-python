#!/usr/bin/env python3
""" Async generator that takes no argument"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generate numbers
        args: void
        Return:
        float time random
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)