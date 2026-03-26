n = int(input())
num = input()

k = 0
sum = 0

while k < n:
    sum += int(num[k])
    k += 1

print(sum)