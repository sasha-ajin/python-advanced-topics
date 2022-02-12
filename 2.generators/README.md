# Generators
Generator is a function, we can pause and start several times and it returns an iterator

If we want to create generator, firstly we should define some function, 
but we're going to use **yield** statement to pause one

## Examples
Let's write one simple generator

```python
def mygenerator():
    print("First item")
    yield 10

    print("Second item")
    yield 20

    print("Last item")
    yield 30
```

Now let's use this generator
```python
gen = mygenerator()

first_number = next(gen) # First item
second_number = next(gen) # Second item
third_number = next(gen) # Last item
# fourth_number = next(gen) # StopIteration error
print(first_number, second_number, third_number) # 10 20 30
```

The generators could not include **return** functions

```python
def mygenerator():
    print("First item")
    yield 10
    # return  # StopIteration error
    print("Second item")
    yield 20

gen = mygenerator()
next(gen)
next(gen)
```

## For loop in generators
The generator function can also use the for loop.
```python
def mygenerator(x):
    for i in range(1, x + 1):
        yield i
```
As you can see above, the **mygenerator** function uses the yield keyword. The generator is called just like a normal function. However, its execution is paused on encountering the **yield** keyword. This sends the first value of the iterator stream to the calling environment. However, local variables and their states are saved internally \
And now we're going to use this generator
```python
gen = mygenerator(3)
for item in gen:
    print(f"{item} item")
```
```
Output:
1 item
2 item
3 item
```

More difficult example
```python
def square_of_sequence(x):
    for i in range(x):
        yield i * i


squres = square_of_sequence(4)
for sqr in squres:
    print(sqr)
```
```
Output:
0
1
4
9
```

## Generator Expression
Python also provides a generator expression, 
which is a shorter way of defining simple generator functions. 
The generator expression is an anonymous generator function

The following is a generator expression for the square_of_sequence() function.
```python
squres = (x * x for x in range(4))

print(next(squres))  # 0
print(next(squres))  # 1
print(next(squres))  # 4
print(next(squres))  # 9
```