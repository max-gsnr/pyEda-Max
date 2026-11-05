def fib(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)
