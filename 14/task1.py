import json
import time
def parse_input():
	blocks = []
	with open("input.txt") as input:
		lines = input.read().splitlines()
	for line in lines:
		corners = [[int(x.split(",")[0]),int(x.split(",")[1])]  for x in line.split(" -> ")]
		for i in range(0, len(corners)-1):
			if corners[i][0] == corners[i+1][0]:
				for j in range(min([corners[i][1], corners[i+1][1]]), max([corners[i][1], corners[i+1][1]]) + 1):
					blocks.append([corners[i][0], j])
			elif corners[i][1] == corners[i+1][1]:
				for j in range(min([corners[i][0], corners[i+1][0]]), max([corners[i][0], corners[i+1][0]]) + 1):
					blocks.append([j, corners[i][1]])
			
	return blocks

initial_blocks = parse_input()
blocks = initial_blocks.copy()
void = sorted(blocks, key=lambda x: x[1])[-1]
current = [500, 0]

while current[1] <= void[1]:
	while current not in blocks:
		if current[1] > void[1]:
			break
		elif [current[0], current[1] + 1] not in blocks:
			current = [current[0], current[1] + 1]
		elif [current[0]-1, current[1] + 1] not in blocks:
			current = [current[0]-1, current[1] + 1]
		elif [current[0]+1, current[1] + 1] not in blocks:
			current = [current[0]+1, current[1] + 1]
		else:
			blocks += [current]
			current = [500, 0]
			
answer = len(blocks)-len(initial_blocks)
print(answer)