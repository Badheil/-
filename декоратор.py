import datetime

def time_decorator(func):
    def wrapper():
        start_time = datetime.datetime.now()
        result = func()
        res = datetime.datetime.now() - start_time
        tre = '{}'.format(res.seconds)
        print(tre)
        return result
    return wrapper

@time_decorator
def sleep_1_sec():
    time.sleep(3)
    print("function")
    return 342
result = sleep_1_sec()
print(result)