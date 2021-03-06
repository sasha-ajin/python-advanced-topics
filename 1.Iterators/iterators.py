"""Iterators are containers for objects so that you can loop over the objects. 
In other words, you can run the "for" loop over the object
"""

### Example ###

"""Let's define some python list"""
num_list = [1, 2, 3, 4, 5]

"""Now we are going to define iterator and go through all the elements of the list"""
simple_iterator = iter(num_list)

print(next(simple_iterator))  # 1
print(next(simple_iterator))  # 2
print(next(simple_iterator))  # 3
print(next(simple_iterator))  # 4
print(next(simple_iterator))  # 5
"""print(next(simple_iterator))  # StopIteration error"""

"""So we can only use iterator once"""

### Create our iterator ###

"""If you want to go through your elements in your class,
you shold create your own iteraor
"""

"""
__iter__()

This method returns the iterator object itself as mentioned above. 
This is required to allow both containers and iterators to be used 
with the for and in statements
"""

"""
__next__()

This method returns the next item from the container. 
If there are no further items, raise the StopIteration exception.
"""


class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return f"{self.counter} step"
        else:
            raise StopIteration


s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)

"""
Output:
1 step
2 step
3 step
4 step
5 step
"""
