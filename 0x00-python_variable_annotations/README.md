# Python Type Annotations

The following is an overview of the essentials of using type annotations in Python 3, including function signatures, variable typing, duck typing, and code validation with `mypy`.

## Table of Contents
- [Type Annotations in Python 3](#type-annotations-in-python-3)
- [Specifying Function Signatures and Variable Types](#specifying-function-signatures-and-variable-types)
- [Duck Typing](#duck-typing)
- [Validating Code with `mypy`](#validating-code-with-mypy)

## Type Annotations in Python 3

Type annotations in Python 3 provide a way to indicate the expected types of variables, function parameters, and return values. Introduced in PEP 484, they allow you to add optional static typing to your Python code without affecting its runtime behavior.

### Type Annotations Basics

Type annotations use the colon syntax for variables and the arrow syntax for function return types:

```python
# Variable annotations
name: str = "Smith"
age: int = 2
coordinates: tuple[float, float] = (34.2, -118.4)

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

## Specifying Function Signatures and Variable Types

Function signatures can be fully annotated to indicate parameter and return types:

```python
from typing import List, Dict, Optional, Union

# Parameter and return type annotations
def process_items(items: List[str], max_length: Optional[int] = None) -> Dict[str, int]:
    result = {}
    for item in items:
        if max_length and len(item) > max_length:
            item = item[:max_length]
        result[item] = len(item)
    return result

# Union types for multiple possible types
def parse_value(value: Union[str, int, float]) -> float:
    return float(value)
```

For more complex types, Python's `typing` module provides:

- Generic containers: `List`, `Dict`, `Tuple`, `Set`
- Special types: `Any`, `Optional`, `Union`, `Callable`
- Type variables with `TypeVar` for generics
- Custom types with `NewType`

## Duck Typing

Duck typing is a programming concept that focuses on what an object can do (its methods and properties) rather than what type it is.

In Python, duck typing means that the compatibility of an object with a given operation is determined by the presence of certain methods or attributes, not by the object's type:

```python
# Duck typing example
def calculate_area(shape):
    # Any object with an area() method will work
    return shape.area()

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Both work despite being different types
circle = Circle(5)
square = Square(4)
print(calculate_area(circle))  # Works
print(calculate_area(square))  # Also works
```

Even with type annotations, Python still uses duck typing at runtime. Type annotations just provide hints for tools and developers without changing the dynamic nature of Python.

## Validating Code with `mypy`

`mypy` is a static type checker for Python that helps catch type-related errors before runtime:

### Installation

```bash
pip install mypy
```

### Basic Usage

```bash
mypy your_script.py
```

### Example of Use

Given this code with type annotations:

```python
# example.py
def add(a: int, b: int) -> int:
    return a + b

result = add("hello", 5)  # Type error
```

Running `mypy`:

```bash
$ mypy example.py
example.py:4: error: Argument 1 to "add" has incompatible type "str"; expected "int"
```

### Configuration

Create a `mypy.ini` file to customize checks:

```ini
[mypy]
python_version = 3.9
warn_return_any = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
```

### Gradual Typing

You can add types incrementally to your codebase:

```python
# Explicitly mark a function as untyped
@typing.no_type_check
def legacy_function(param):
    return param
```

Type annotations combined with tools like `mypy` help catch errors earlier in development while maintaining Python's flexibility.