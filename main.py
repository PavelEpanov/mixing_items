L = [1, 2, 3]

for x in range(len(L)):
	L = L[1:] + L[:1]
	print(L)

S = "spam"

for x in range(len(S)):
	S = S[1:] + S[:1]
	print(S, end=" ")

