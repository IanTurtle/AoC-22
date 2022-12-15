import re
import time
import json

def parse_input():
	x = []
	pattern = re.compile(r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)")
	with open("input.txt") as input:
		lines = input.read().splitlines()
	for line in lines:
		search = pattern.search(line)
		x.append([[int(search.group(1)), int(search.group(2))], [int(search.group(3)), int(search.group(4))]])
	return x

def get_max_coord_at_height(sensor, distance, y, limit):
	if abs(y-sensor[1]) > distance:
		return []
	min_x = sensor[0] - (distance - abs(y-sensor[1]) - 1)
	max_x = sensor[0] + (distance - abs(y-sensor[1]) - 1) 
	if max_x > limit:
		max_x = limit
	return [max_x, y]

def calculate_distance(sensor, point):
	return abs(point[0]-sensor[0]) + abs(point[1]-sensor[1]) + 1
	
coords = parse_input()
beacons = set([str(beacon) for _, beacon in coords])
max_distances = [[sensor, calculate_distance(sensor, beacon)] for sensor, beacon in coords]
missing = []
n = 4000000

y = 0
while y < n+1:
	x = 0
	while x < n+1:
		point = [x,y]
		point_covered = False
		for sensor, max_distance in max_distances:
			from_sensor = calculate_distance(sensor, point)
			if from_sensor <= max_distance:
				point_covered = True
				max_x = get_max_coord_at_height(sensor, max_distance, y, n+1)
				x = max_x[0]
				break	
		if not point_covered:
			missing = [x, y]
			break
		x += 1
	if missing:	
		break
	y += 1

answer = (missing[0] * 4000000) + missing[1]
print(answer)