import math

with open("input.txt") as input:
	steps = [ (step.split(" ")[0], int(step.split(" ")[1])) for step in input.read().splitlines()]

def update_position(position, step):
	dir = step[0]
	amount = step[1]
	
	match dir:
		case 'R':
			new_positions = [[position[0] + i, position[1]] for i in range(1, amount+1)]
		case 'U': 
			new_positions = [[position[0], position[1] + i] for i in range(1, amount+1)]
		case 'L': 
			new_positions = [[position[0]-i, position[1]] for i in range(1, amount+1)]
		case 'D':
			new_positions = [[position[0], position[1] - i] for i in range(1, amount+1)]
	return new_positions
	
def update_tail_position(head_position, tail_position):
	difference = (head_position[0] - tail_position[0], head_position[1] - tail_position[1])
	new_position = tail_position
	if abs(difference[0]) <=1 and abs(difference[1]) <=1:
		return new_position
	else:
		if difference[0]:
			new_position[0] = new_position[0] + int(math.copysign(1, difference[0]))	
		if difference[1]:
			new_position[1] = new_position[1] + int(math.copysign(1, difference[1]))
		return new_position
	
	
# x, y position
positions = [[0, 0]]
tail = [0, 0]

for step in steps:
	position = positions[-1]
	positions += update_position(position, step)

tail_positions = []
tail_position = [0, 0]

for head in positions[1:]:
	tail = update_tail_position(head, tail)
	tail_positions.append(str(tail))
answer = len(set(tail_positions))
print(answer)