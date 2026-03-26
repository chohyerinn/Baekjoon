import sys

input = sys.stdin.readline

n = int(input())
books = {}

for _ in range(n):
    title = input().strip()
    books[title] = books.get(title, 0) + 1

max_count = max(books.values())

candidates = []
for title in books:
    if books[title] == max_count:
        candidates.append(title)

print(sorted(candidates)[0])