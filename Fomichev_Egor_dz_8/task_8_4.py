from functools import wraps


def val_checker(val_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if val_func(*args):
                return func(*args)
            else:
                msg = f'wrong value {", ".join(map(str, args))}'
                raise ValueError(msg)

        return wrapper

    return _val_checker
