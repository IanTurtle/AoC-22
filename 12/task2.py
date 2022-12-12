import time

class Node():
	
	def __init__(self, x, y, value):
		self.x = x
		self.y = y
		self.value = value
		self.children = []

	def add_node(self, node):
		self.children.append(node)

	def __str__(self):
		return f"{self.x},{self.y}"
		
	def __repr__(self):
		return f"{self.x},{self.y}"

nodes = []
with open("input.txt") as input:
	lines = input.read().splitlines()
	
for i in range(0, len(lines)):
	line = lines[i]
	line_nodes = []
	for j in range(0, len(line)):
		height = line[j]
		if height == "S":
			line_nodes.append(Node(i, j, ord('a')))
		elif height == "E":
			start = Node(i, j, ord('z')+1)
			line_nodes.append(start)
		else:
			line_nodes.append(Node(i, j, ord(height)))
	nodes.append(line_nodes)

for i in range(0, len(nodes)):
	line = nodes[i]
	for j in range(0, len(line)):
		node = nodes[i][j]
		adjacent_indices = [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]
		for x, y in adjacent_indices:
			if x >= 0 and x < len(nodes) and y >= 0 and y < len(line):
				adjacent = nodes[x][y]
				if adjacent.value >= node.value - 1:
					node.add_node(adjacent)
		

unvisited = [node for row in nodes for node in row if node]
distances = {node: 99999999999 for row in nodes for node in row if node}


node = start
distances[start] = 0
distance = distances[start]
while unvisited:
	unvisited_neighbors = [node for node in node.children if node in unvisited]
	for neighbor in unvisited_neighbors:
		if distances[neighbor] > distance:
			distances[neighbor] = distance
	unvisited.remove(node)
	if node.value == ord('a'):
		break
	else:
		unvisited_distances = sorted([[node, distance] for node, distance in distances.items() if node in unvisited], key=lambda x: x[1])			
		node = unvisited_distances[0][0]
		distance = distances[node] + 1
answer = distance
print(answer)