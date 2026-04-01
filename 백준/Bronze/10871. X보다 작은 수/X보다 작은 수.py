import sys

N, X = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

for i in nums:
    if i < X:
        print(i, end=' ')