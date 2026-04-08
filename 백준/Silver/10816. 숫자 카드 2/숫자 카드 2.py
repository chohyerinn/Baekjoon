n = int(input())
cards = list(map(int, input().split()))

count = {}
for num in cards:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

m = int(input())
targets = list(map(int, input().split()))

for num in targets:
    if num in count:
        print(count[num], end=' ')
    else:
        print(0, end=' ')