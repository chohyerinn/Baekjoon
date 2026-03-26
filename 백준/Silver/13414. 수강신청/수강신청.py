import sys

K, L = map(int, input().split())

last = {}

for i in range(L):
    student = sys.stdin.readline().strip()
    last[student] = i

result = sorted(last.items(), key=lambda x: x[1])

for student, _ in result[:K]:
    print(student)