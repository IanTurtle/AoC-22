import re

def parse_input():
	with open("input.txt") as input:
		assignments = input.read().splitlines()
		
	pattern = re.compile(r"(\d*)-(\d*),(\d*)-(\d*)")
	pairs = []
	for assignment in assignments:
		result = pattern.search(assignment)
		pairs.append([[int(result.group(1)),int(result.group(2))], [int(result.group(3)),int(result.group(4))]])
	return pairs
	
pairs = parse_input()

contained_pairs = []

highest_number = max([number for pair in pairs for numbers in pair for number in numbers])
for pair in pairs:
	ranges = [0] * (highest_number+1)
	for sections in pair:
		for i in range(sections[0], sections[1]+1):
			ranges[i]+=1
			if ranges[i] > 1:
				contained_pairs.append(pair)
				break
				
answer = len(contained_pairs)
print(answer)