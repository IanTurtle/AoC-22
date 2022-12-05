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

parse_input()
crates, moves = parse_input()

for move in moves:
	count, src, dest = parse_instruction(move)
	
	crate = crates[src][-count:]	
	crates[src] = crates[src][:-count]
	crates[dest] += crate

answer = ""

for row in crates:
	answer += row[-1]
	
print(answer)

