import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    cut = int(n * 0.15 + 0.5)

    arr = arr[cut:n-cut]

    avg = int(sum(arr) / len(arr) + 0.5)

    print(avg)