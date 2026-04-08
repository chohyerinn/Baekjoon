from collections import deque

n = int(input())
cards = deque(range(1, n+1))

while len(cards) > 1:
    cards.popleft()            # 맨 위 버림
    cards.append(cards.popleft())  # 다음 카드 뒤로

print(cards[0])