def print_args(func):
    def inner_func(*args, **kwargs):
        print(f'args {args}')
        print(f'kwargs {kwargs}')
        return func(*args, **kwargs) #Call the original function with its arguments.
    return inner_func

@print_args
def multiply(num_a, num_b):
    return num_a * num_b


class Decorator(object):
    """Simple decorator class."""
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        print(f'args {args}')
        print(f'kwargs {kwargs}')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res
@Decorator
def testfunc():
    print('Inside the function.')


if __name__ == '__main__':
    multiply(3,3)
    testfunc()




