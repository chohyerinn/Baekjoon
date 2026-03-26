import sys

N, M = map(int, sys.stdin.readline().split())

word_count = {}

for _ in range(N):
    word = sys.stdin.readline().strip()

    if len(word) >= M:
        word_count[word] = word_count.get(word, 0) + 1

result = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in result:
    print(word)