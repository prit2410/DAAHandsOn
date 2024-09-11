def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# Debugging fib(5)
def fib_debug(n):
    call_stack = []

    def inner_fib(m):
        call_stack.append(f'fib({m})')
        if m == 0:
            return 0
        if m == 1:
            return 1
        return inner_fib(m - 1) + inner_fib(m - 2)

    result = inner_fib(n)
    return call_stack, result


call_stack, result = fib_debug(5)
print("Call Stack:", " -> ".join(call_stack))
print("Result:", result)
