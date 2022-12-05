import re

pattern = re.compile(r"move (\d*) from (\d*) to (\d*)")

def parse_input():
	crates_raw = []
	with open("input.txt") as input:
		line = input.readline().replace("\n", " ")
		while line != " ":
			line_split = [line[i:i+4][1] for i in range(0, len(line), 4)]
			crates_raw.append("".join(line_split))
			line = input.readline().replace("\n", " ")
			
		moves = input.read().splitlines()
	input.close()
	print(crates_raw)
	# Convert the list of crates to a list of moves
	input_length = len(crates_raw[-1]) # not great - since this only works with lists length < 10	
	crates = [[] for _ in range(input_length)]
	_x = crates_raw[:-1]
	_x.reverse()
	for i in range(len(_x)):
		row = list(_x[i])
		for j in range(len(row)):
			crate = row[j]
			if crate != " ":
				crates[j].append(row[j])
	
	return crates, moves

def parse_instruction(instruction):
	result = pattern.search(instruction)
	
	count = int(result.group(1))
	src = int(result.group(2))-1
	dest = int(result.group(3))-1
	
	return count, src, dest

crates, moves = parse_input()
print(crates)
for move in moves:
	count, src, dest = parse_instruction(move)
	for i in range(count):
		crate = crates[src].pop()
		crates[dest].append(crate)

answer = ""
for row in crates:
	answer += row[-1]
	
print(answer)

