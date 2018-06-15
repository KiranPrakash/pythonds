def fibonacci(n):
    memo = [None]*1000
    if memo[n] is not None:
        return memo[n]
    elif n < 2:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        memo[n] = result
    return result

