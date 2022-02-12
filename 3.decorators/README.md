# Decorators
Decorators're kind of "wrapper" of the method, which adds  responsibilities or functionalities 
to a method dynamically without modifying a function. \
So basically, decorator determines what is going to happen before and after method 

## Examples
To understand how decorators works and their purpose,let's define 2 function with the same start part

```python
def welcome():
    print(f"hello, welcome!")

def question():
    print(f"hello, how are you?!")

welcome() # hello, welcome!
question() # hello, how are you?!
```
As you can see, both methods have "Hello, " at the start of the print and "!" at the and,
so we can define the kind of "wrapper" for those functions to follow **DRY** rule

Function is the decorator, when it is the function that takes a function (any function that does not take any argument) 
as an argument. The inner function **inner_function()** can access the outer function's argument, 
so it executes some code before or after to extend the functionality before calling the argument function.
```python
def hello(fn):
    def inner_function():    
        print(f"hello, ", end="")    
        fn()
        print("!")
    return inner_function
```
And now we should define welcome and question methods, which're going to use hello decorator
```python
@hello
def welcome():
    print(f"welcome", end="")

@hello
def question():
    print(f"how are you?", end="")

welcome() # hello, welcome!
question() # hello, how are you?!
```
## Decorators with arguments
What if in our methods we will add some parameter, for example: **name**
The same part is going to be "hello, <name>, " at the start, and "!" at the end are the same parts
So we should add name argument to our hello decorator

The syntax for decorators with arguments is a bit different, we should make "wrapper"  
to our previous decorator, which, is going take name argument
```python
def hello(name):
    def decorator(fn):
        def inner_function():    
            print(f"hello, {name}, ", end="")    
            fn()
            print("!")
        return inner_function
    return decorator
```
And now let's define our functions
```python
@hello("Ivan")
def ivan_welcome():
    print(f"welcome", end="")

@hello("Ivan")
def ivan_question():
    print(f"how are you?", end="")


ivan_welcome() # hello, Ivan, welcome!
ivan_question() # hello, Ivan, how are you?!
```
## Getting argument from input function in decorator
But what if we want to create welcome and question functions, where we will pass name argument
and return "hello, < name >, < function print >!" output

In our decorator we should get first argument from args list and write it  
```python
def hello(fn):
    def inner_function(*args, **kwargs):
        print(f"hello, {args[0]}, ", end="")
        fn(*args, **kwargs)
        print("!")
    return inner_function
```
We should write name argument in our methods
```python
@hello
def welcome(name):
    print("welcome", end="")

@hello
def question(name):
    print("how are you?", end="")

welcome("Ivan") # hello, Ivan, welcome!
question("Ivan") # hello, Ivan, how are you?!
```