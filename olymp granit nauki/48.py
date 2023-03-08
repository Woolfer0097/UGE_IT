def foo(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return n + foo(n - 1)
        else:
            return 2 * foo(n - 2)


print(foo(26))
