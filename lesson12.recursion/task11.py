def fib(n):
    if n in (1, 0):
        return n
    return fib((n - 1)) + fib((n - 2))


print(fib(15))


