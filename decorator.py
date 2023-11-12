from typing import Callable
from functools import wraps

previous_results = {}
inputs_order = []


def memoized(n: int):
    def wrapped(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            if args in previous_results.keys():
                return previous_results[args]

            result = func(*args, **kwargs)

            if n:
                if len(inputs_order) <= n:
                    previous_results[args] = result
                    inputs_order.append(args)

                else:
                    del previous_results[inputs_order[0]]
                    previous_results[args] = result

                    for i in range(n - 1):
                        inputs_order[i] = inputs_order[i + 1]

                    inputs_order[n - 1] = args

            else:
                previous_results[args] = result

            return result

        return inner

    return wrapped


if __name__ == '__main__':
    @memoized(5)
    def f(x: int):
        print('Calculating...')
        return x * 10

    for i in range(5):
        print(f(i))
    for i in range(5):
        print(f(i))
    print(f(6))
    print(f(6))
