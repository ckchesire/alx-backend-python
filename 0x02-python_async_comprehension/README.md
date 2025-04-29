```markdown
# Python Async Generators & Comprehensions Guide

This repository demonstrates how to use asynchronous generators, async comprehensions, and how to type-annotate both regular and async generators in Python.

## Asynchronous Generators

An asynchronous generator is defined using `async def` and `yield`, and allows `await` inside the generator.

```python
import asyncio

async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i
```

### Consuming an Async Generator

```python
async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())
```

## Async Comprehensions

Async comprehensions work similarly to regular comprehensions but allow asynchronous iteration.

```python
async def async_generator():
    for i in range(3):
        await asyncio.sleep(0.5)
        yield i

async def main():
    result = [i async for i in async_generator()]
    print(result)

asyncio.run(main())
```

## Type Annotations

### Regular Generator

Use `Generator` from the `typing` module.

```python
from typing import Generator

def gen_numbers() -> Generator[int, None, None]:
    yield 1
    yield 2
```

### Async Generator

Use `AsyncGenerator` from the `typing` module.

```python
from typing import AsyncGenerator

async def async_gen() -> AsyncGenerator[int, None]:
    for i in range(3):
        await asyncio.sleep(1)
        yield i
```

## Requirements

- Python 3.6+
- No external dependencies

## Running the Examples

Save the code examples in a file like `async_example.py` and run:

```bash
python async_example.py
```

Make sure your script uses `asyncio.run(main())` at the entry point.
