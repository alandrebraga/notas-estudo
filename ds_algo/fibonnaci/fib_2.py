def fib_list(n):
    """
    T(n) = 2n + 2
    entao T(100) = 202
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[-1]


print(fib_list(100))
