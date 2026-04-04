import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip())

def digit_sum(s):
    total = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
    return total

arr.sort(key=lambda x: (len(x), digit_sum(x), x))

for s in arr:
    print(s)