import sys

input = sys.stdin.readline

n = int(input())
ext_count = {}

for _ in range(n):
    filename = input().strip()
    ext = filename.split('.')[1]   # 점이 정확히 한 번만 나온다고 했음
    
    if ext in ext_count:
        ext_count[ext] += 1
    else:
        ext_count[ext] = 1

for ext in sorted(ext_count):
    print(ext, ext_count[ext])