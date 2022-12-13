import json

def parse_input():
	x = []
	with open("input.txt") as input:
		lines = input.read().splitlines()
	for i in range(0, len(lines), 3):
		x.append([json.loads(lines[i]), json.loads(lines[i+1])])
	return x

def compare(left_packet, right_packet):
	status = "same"
	while left_packet and right_packet:
		
		left = left_packet.pop(0)
		right = right_packet.pop(0)
		if isinstance(left, int) and isinstance(right, int):
			if left < right:
				status = "left"
				break
			elif right < left:
				status = "right"
				break
			else:
				status = "same"
		elif isinstance(left, list) and isinstance(right, list):
			status = compare(left, right)
		elif isinstance(left, list):
			status = compare(left, [right])
		else:
			status = compare([left], right)	
		if status != "same":
			return status
			
	if status == "same":
		if not left_packet and not right_packet:
			status = "same"
		elif left_packet: 
			status = "right"
		else:
			status = "left"
	return status

packets = parse_input()
index = 1
answer = 0
for i in range(0, len(packets)):
	pair = packets[i]
	result = compare(pair[0], pair[1])
	if result == "left":
		answer += (i+1)

print(answer)