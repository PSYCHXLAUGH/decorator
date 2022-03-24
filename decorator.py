def decorator(function_id):
    def wrapper():
        print(function_id() + " decorator")
    
    return wrapper


@decorator # equal test = decorator(test)
def test():
    return "hello"


test()