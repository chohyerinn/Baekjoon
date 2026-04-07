N = int(input())

count = 1      # 방 개수 (층)
lastN = 1      # 현재 층의 마지막 숫자

while N > lastN:
    lastN += 6 * count
    count += 1

print(count)