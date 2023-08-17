def fib_recursive(n):
    """
    sendo T(n) o numero de linhas que algoritimo roda
    se n <= 1 então 2 linhas
    se n >= 2 então T(n) = 3+T(n -1) + t(n-1)
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
