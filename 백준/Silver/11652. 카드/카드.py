import sys

n = int(sys.stdin.readline())
cards = {}

for _ in range(n):
    num = int(sys.stdin.readline())
    
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

answer = None
max_count = 0

for num, count in cards.items():
    if count > max_count:
        max_count = count
        answer = num
    elif count == max_count:
        if num < answer:
            answer = num

print(answer)