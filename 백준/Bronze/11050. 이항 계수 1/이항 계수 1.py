n, k = map(int, input().split())

def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

answer = factorial(n) // (factorial(k) * factorial(n - k))

print(answer)