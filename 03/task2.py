import string

with open("input.txt") as input:
	all_backpacks = input.read().splitlines()

answer = 0
for i in range(0, len(all_backpacks)-1, 3):
	backpacks = all_backpacks[i:i+3]
	one = set(backpacks[0])
	two = set(backpacks[1])
	three = set(backpacks[2])

	dOne = (one - (one - two))
	dTwo = (two - (two - three))

	unique = list(dOne - (dOne - dTwo))[0]
	answer += (string.ascii_letters.index(unique)+1)

print(answer)