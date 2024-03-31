# ARGUMENT CHECKING DECORATOR :
from functools import wraps

def arg_checker(*arg_types):
    '''An argument checker decorator checks both:
    - The no. of variable that u used for a function
    - The type of each variables'''
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) != len(arg_types):
                raise TypeError(f'Function{func.__name__} takes {len(arg_types)}')
            for arg, arg_types in zip(arg, arg_types):
                if not isinstance(arg, arg_types):
                    raise TypeError(f'{func.__name__} expected a positional value of {func.__doc__}')
            return func(*args)
        return wrapper
    return decorator


