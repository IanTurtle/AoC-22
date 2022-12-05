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
contained_pairs = [ 
					pair for pair in pairs 
					if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]) 
				]
				
answer = len(contained_pairs)
print(answer)
	