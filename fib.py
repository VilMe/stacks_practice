


def fib(something, n_times):
    while n_times > 0:
        print(something, n_times)
        return fib(something, n_times - 1)



fib('hhhhhell world', 4)