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
	
	
# all x, y positions for all knots
positions = [[[0,0] for i in range(0, 10)]]
all_knot_positions = positions[0]
tail_positions = []
for step in steps:
	# calculate all new head positions 
	new_head_positions = update_position(all_knot_positions[0], step)
	
	# for each new head position, calculate the position of the rest of the nots
	for head_position in new_head_positions:
		new_knot_positions = [head_position] + positions[-1][1:]
		
		for i in range(1, len(new_knot_positions)):
			new_knot_positions[i] = update_tail_position(new_knot_positions[i-1], new_knot_positions[i].copy())

		positions.append(new_knot_positions)
		tail_positions.append(str(new_knot_positions[-1]))
		all_knot_positions = positions[-1]


answer = len(set(tail_positions))
print(answer)