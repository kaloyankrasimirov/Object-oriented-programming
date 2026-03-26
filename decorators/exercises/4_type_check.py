def type_check(params):
    def decorator(func):
        def wrapper(param):
            if not isinstance(param, params):
                return "Bad Type"
            return func(param)
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
