# Type hinting

Some programming languages have static typing, such as C/C++. It means that you need to declare types of variables, parameters, and return values of a function upfront.
The predefined types allow the compilers to check the code before
compiling and running the program.

Python uses dynamic typing, in which variables, parameters, andreturn values of a function can be any type. Also, the types of variables can change while the program runs.

Generally, dynamic typing makes it easy to program and causes unexpected errors that you can only discover until the program runs.

Python’s type hints provide you with optional static typing to leverage the best of both static and dynamic typing.It makes your code to be more readable, clear and helps to find errors earlier

## Variables

This is how you declare the type of a variable type in Python 3.6

```python
age: int = 5
```

You don't need to initialize a variable to annotate it

```python
age: int 
```

Let's look at all python types

```python
boolean_var: bool
string_var: str
float_var: float
comlex_var: complex
bytes_var: bytes
```

## Functions

This is how you annotate a function definition

```python
def stringify(num: int) -> str:
    return str(num)

print(stringify(2))  # 2
```

And here's how you specify multiple arguments

```python
def add(num1: int, num2: int) -> int:
    return num1 + num2

print(add(num1=2, num2=3))  # 5
```

Sometimes argument can be integers or floats.
To set type hints for multiple types, you can use Union from the typing module.

```python
from typing import Union


def add(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2


print(add(num1=2, num2=3.5))  # 5.5
```

Python allows you to assign an alias to a type and use the alias for type hintings.
For example:

```python
number = Union[int, float]

def add(x: number, y: number) -> number:
    return x + y
```

Now add type hints by annotating the arguments and the return value as follows:

```python
def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


print(headline("python type checking", align="left"))
print(headline("python type checking", align="center"))
print(headline("python type checking", align=False))
```

Output:

```
Python Type Checking
--------------------
Python Type Checking
--------------------
oooooooooooooo Python Type Checking oooooooooooooo
```

So if type is not bool, argument'll take default value

## Classes

Also you can use type hinting in classes in definition of the
python classe.For example:

```python
class MyClass:
    """You can optionally declare instance variables in the class body"""
    attr: int
    """This is an instance variable with a default value"""
    charge_percent: int = 100

    """The '__init__' method doesn't return anything, so it gets return
    type 'None' just like any other method that doesn't return anything"""
    def __init__(self) -> None:
        pass

    """For instance methods, omit type for 'self'"""
    def my_method(self, num: int, str1: str) -> str:
        return num * str1
```

User-defined classes are valid as types in annotations

```python
x: MyClass = MyClass()
```

## Using a static type checker tool: mypy

Python doesn’t have an official static type checker tool.
So, if you will give int argument to string argument, interpreter
will not return you an error
At the moment, the most popular third-party tool is Mypy.
Since Mypy is a third-party package, you need to install it using
pip, and start program with it
