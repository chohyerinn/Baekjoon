import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split())) 

MAX_VAL = -10**9 - 1
MIN_VAL =  10**9 + 1

def dfs(idx, val, plus, minus, mul, div):
    global MAX_VAL, MIN_VAL
    if idx == N:
        MAX_VAL = max(MAX_VAL, val)
        MIN_VAL = min(MIN_VAL, val)
        return
    if plus:
        dfs(idx+1, val + A[idx], plus-1, minus, mul, div)
    if minus:
        dfs(idx+1, val - A[idx], plus, minus-1, mul, div)
    if mul:
        dfs(idx+1, val * A[idx], plus, minus, mul-1, div)
    if div:
        dfs(idx+1, int(val / A[idx]), plus, minus, mul, div-1)

dfs(1, A[0], ops[0], ops[1], ops[2], ops[3])
print(MAX_VAL)
print(MIN_VAL)