
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)

print(find_sum(15))

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n - 2)

print(fib(15))
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))