import json
import functools

def parse_input():
	with open("input.txt") as input:
		lines = [ json.loads(line) for line in input.read().splitlines() if line ]
	lines += [[[2]], [[6]]]
	return lines

def compare(left_packet, right_packet):
	status = 0
	l = left_packet.copy()
	r = right_packet.copy()
	while l and r:
		
		left = l.pop(0)
		right = r.pop(0)
		if isinstance(left, int) and isinstance(right, int):
			if left < right:
				status = -1
				break
			elif right < left:
				status = 1
				break
			else:
				status = 0
		elif isinstance(left, list) and isinstance(right, list):
			status = compare(left, right)
		elif isinstance(left, list):
			status = compare(left, [right])
		else:
			status = compare([left], right)	
		if status != 0:
			return status
			
	if status == 0:
		if not l and not r:
			status = 0
		elif l: 
			status = 1
		else:
			status = -1
	return status

packets = parse_input()
sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))
answer = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
print(answer)