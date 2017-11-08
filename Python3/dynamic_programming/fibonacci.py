# Fibonacci
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_dp(n):
    fib_val = [0,1]
    if n < 2:
        return fib_val[n]
    for x in range(2,n+1):
        fib_val.append(fib_val[x-1] + fib_val[x-2])
    return fib_val[n]

def fib_dp2(n): # Why cannot execute..;;
    fib_val = [0 for i in range(0, n+1)]
    if fib_val[n] != 0:
        return fib_val[n]
    if n == 1 or n == 2:
        fib_val[n] = 1
    else:
        fib_val[n] = fib_val[n-1] + fib_val[n-2]
    return fib_val[n]