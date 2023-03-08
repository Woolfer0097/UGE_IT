def foo(a, b):
    s = a + b

    def bar(s, b):
        k = s * b
        if k % 2 == 0:
            return foo(b, s)
        return k + b

    return bar(s, a)


print(foo(3, 3))
