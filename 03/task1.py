import string

with open("input.txt") as input:
	backpacks = input.read().splitlines()

answer = 0
for backpack in backpacks:
	one, two = set(backpack[:len(backpack)//2]), set(backpack[len(backpack)//2:])
	unique = list(one - (one - two))[0]
	answer += (string.ascii_letters.index(unique)+1)

print(answer)