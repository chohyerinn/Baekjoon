T=int(input())

for _ in range(T):
	A = list(map(int, input().split()))

	B = A.copy()
	B.remove(max(A))
	B.remove(min(A))

	if max(B)-min(B)>=4:
		print("KIN")
	
	else:
		s = sum(A)-max(A)-min(A)
		print(s)
	