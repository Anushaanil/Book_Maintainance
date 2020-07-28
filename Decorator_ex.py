from math import fsum
from typing import Callable,List,Set
from functools import wraps
from time import perf_counter
def stop_watch(func:Callable) ->Callable:
    times=[]
    @wraps(func)
    def inner(*args,**kwargs):
        for _ in range(10):
            start_time = perf_counter()
            func(*args,**kwargs)
            end_time = perf_counter()
            elapsed = end_time - start_time
        times.append(elapsed)
        average_time = fsum(times) / len(times)
        print(f"Average elapsed time for executing {func.__name__} is {average_time:.5f}")
    return inner
@stop_watch
def make_list(size:int) -> List:
    return list(range(size))

@stop_watch
def make_set(size:int) -> Set:
    return set(range(size))

make_list(100_000)
make_set(100_000)
'''
def example_decorator(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        print(f"For {func.__name__} code execution time was around {end_time - start_time:.5f} seconds")
    return inner
@example_decorator
def add(*args, **kwargs):
    print(sum(*args, **kwargs))

@example_decorator
def add(*args, **kwargs):
    print(sum(*args, **kwargs))

add([1, 5, 7, 4, 8])
add([200, 345])
print(add)  # with wraps name get reserved

# can find sum of any number of values using decorators
# print(add) without wraps gives <function example_decorator.<locals>.inner at 0x03130780>
print("And the sum is:", func(*args,**kwargs))
def add(*args,**kwargs):return sum(*args,**kwargs) 
can be used to print the sum but we can directly use the value obtained from inner using return inside it

def example_decorator(func: Callable) -> Callable:
    def inner(): #without arguments
        pass
    return inner
@example_decorator
def greeting():
    pass
greeting()
# print(example_decorator(greeting)) gives <function example_decorator.<locals>.inner at 0x03130780>
# print(greet) gives the reference obj of this func instead just call greet()
# which takes up greeting fn and pass it to our decorator
# greet = example_decorator(greeting)  greet() This approach bcms clumsy to use 
so, we can use @decorator_name on the func which we want to call inside our decorator func
'''