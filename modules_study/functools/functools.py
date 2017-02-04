from functools import reduce, singledispatch

# A number of tools in Python accept key functions to control how elements are ordered or grouped. They include min(), max(), sorted(), list.sort(), heapq.merge(), heapq.nsmallest(), heapq.nlargest(), and itertools.groupby().
# mm = functools.cmp_to_key()
#
# sorted([111,12,12,134,506,78], key=cmp_to_key(lambda x, y: y-x))


# @lru_cache
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)


# @total_ordering

# basetwo = partial(int, base=2)
# print basetwo

# class Cell(object):
#      def __init__(self):
#          self._alive = False
#      @property
#      def alive(self):
#          return self._alive
#      def set_state(self, state):
#         self._alive = bool(state)
#         set_alive = partialmethod(set_state, True)    set_dead = partialmethod(set_state, False)

# mm = reduce(lambda x, y: x+y, [1,2,3,4,5])
# print mm

@singledispatch
def func(arg, verbose=Flase):
    if verbose:
        print 'let me say,', end=""

    print arg

@fun.register(int)
fun.register(type(None), nothing)
fun.registry.keys()

from functools import wraps
def my_decorator(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         print('Calling decorated function')
         return f(*args, **kwds)
     return wrapper

@my_decorator
 def example():
     """Docstring"""
     print('Called example function')



