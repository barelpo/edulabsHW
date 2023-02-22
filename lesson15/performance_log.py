import datetime


def performance_log(orig_func):

    def wrapping_func(*args, **kwargs):
        start = datetime.datetime.now()
        orig_func(*args, **kwargs)
        finish = datetime.datetime.now()
        print(finish - start)

    return wrapping_func


@performance_log
def my_foo(num):
    return num ** 100000000


if __name__ == "__main__":
    my_foo(2)
