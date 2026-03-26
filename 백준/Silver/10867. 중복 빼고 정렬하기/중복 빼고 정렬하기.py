N = int(input())
A = list(map(int, input().split()))

A = sorted(set(A))

for x in A:
    print(x, end=' ')