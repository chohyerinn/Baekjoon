N = int(input())
first = input()

first_count = [0] * 26
for ch in first:
    first_count[ord(ch) - ord('A')] += 1

answer = 0

for _ in range(N - 1):
    word = input()

    word_count = [0] * 26
    for ch in word:
        word_count[ord(ch) - ord('A')] += 1

    diff = 0
    for i in range(26):
        diff += abs(first_count[i] - word_count[i])

    if diff == 0:
        answer += 1
    elif diff == 1:
        answer += 1
    elif diff == 2 and len(first) == len(word):
        answer += 1

print(answer)