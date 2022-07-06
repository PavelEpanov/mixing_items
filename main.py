L = [1, 2, 3]

for x in range(len(L)):
	L = L[1:] + L[:1]
	print(L)

S = "spam"

for x in range(len(S)):
	S = S[1:] + S[:1]
	print(S, end=" ")


# Обычная функция
def scramble(seq):
	res = []
	for i in range(len(seq)):
		res.append(seq[i:] + seq[:i])
	return res

print(scramble("spam"))

def scramble2(seq):
	return [seq[i:] + seq[:i] for i in range(len(seq))]

print(scramble2("spam"))

for x in scramble((1, 2, 3)):
	print(x, end=" ")

# Функция генератор

def scramble3(seq):
	for i in range(len(seq)):
		seq = seq[i:] + seq[:i]
		yield seq
print(list(scramble3("spam")))

def scramble4(seq):
	for i in range(len(seq)):
		yield seq[i:] + seq[:i]

print(list(scramble4("spam")))

for x in scramble4((1, 2, 3)):
	print(x)

print(list(scramble4((1, 2, 3))))

# Списковое включение

PP = "spam"
PPP = (PP[i:] + PP[:i] for i in range(len(PP)))
print(list(PPP))

