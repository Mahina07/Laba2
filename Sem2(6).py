import functools
def cache_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global cache_map
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        key = ", ".join(args_repr + kwargs_repr)
        if key in cache_map:
            return cache_map[key]
        else:
            value = func(*args, **kwargs)
            cache_map[key] = value
            return value
    return wrapper

@cache_function
def factorial(n: int) -> int:
    return n * factorial(n - 1) if n >= 1 else 1