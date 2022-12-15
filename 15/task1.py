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

def get_coords_at_height(sensor, distance, y):
	if abs(y-sensor[1]) > distance:
		return []
	min_x = sensor[0] - (distance - abs(y-sensor[1]) - 1)
	max_x = sensor[0] + (distance - abs(y-sensor[1]) - 1) 
	x = min_x
	
	coords = []
	while x <= max_x:
		coords.append([x, y])
		x+= 1
	return coords
	
coords = parse_input()
beacons = set([str(beacon) for _, beacon in coords])
all_coords = []
n = 2000000
for sensor, beacon in coords:
	distance = abs(beacon[0]-sensor[0]) + abs(beacon[1]-sensor[1]) + 1
	coordinates = get_coords_at_height(sensor, distance, n)
	all_coords += coordinates
	
beaconless_coords = [json.loads(coord) for coord in (set([str(x) for x in all_coords]) - beacons)]
answer = len(beaconless_coords)
print(answer)