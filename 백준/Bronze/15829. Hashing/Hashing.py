
L = int(input())
str = input()

r = 31
m = 1234567891

power = 1
result = 0

for i in range (L) : 
	num = ord(str[i]) -96  #ASCII 기준 a 는 97. 근데 a=1 로 만들어야해서
	result = result + num*power
	power = power * r

print(result%m)