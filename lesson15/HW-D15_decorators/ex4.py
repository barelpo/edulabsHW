class InvalidArgument(Exception):
    pass


def numeric_in_range(min_num, max_num):

    def f1(orig_func):

        def f2(*args, **kwargs):
            for arg in args + tuple(kwargs.values()):
                if type(arg) in (int, float) and arg not in range(min_num, max_num + 1):
                    raise InvalidArgument()
            return orig_func(*args, **kwargs)

        return f2

    return f1


@numeric_in_range(1, 5)
def foo(num1):
    print(num1 ** 2)


if __name__ == "__main__":
    try:
        foo(4)
    except InvalidArgument:
        print("Argument not in range between 1 and 5!")
