from inspect import getcallargs
import datetime
import time
def logging_decorator(logger: list()):
    def decorator(func):
        def wrapper(*args, **kwargs):
            d = {}
            _time = datetime.datetime.now()
            result = func(*args, **kwargs)
            d['name'] = func.__name__
            d['arguments'] = getcallargs(func, *args, **kwargs)
            d['call_time'] = _time
            d['result'] = result
            logger.append(d)
            return result
        return wrapper
    return decorator
logger = []

# @logging_decorator(logger)
# def test_simple(a=[1,2,3,4], b = 2):
#     return 127

# test_simple() 
# print(logger)


# signature = inspect.signature(func)
# s = ''.join('{}: {}'.format(k, v) for k,v in signature.parameters.items() if v.default is not inspect.Parameter.empty)
# print(s)
# a = inspect.getargspec(func)
# print(a.defaults)