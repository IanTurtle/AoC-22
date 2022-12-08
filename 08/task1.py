with open("input.txt") as input:
	trees = [[int(height) for height in row ] for row in input.read().splitlines()]

def get_surrounding_trees(x, y, trees):
	row = trees[x]
	col = [tree[y] for tree in trees]
	left = row[:y]
	right = row[y+1:]
	top = col[:x]
	bottom = col[x+1:]
	return [left, right, top, bottom]

def is_tree_visible(x, y, trees):
	tree = trees[x][y]
	surrounding_trees = get_surrounding_trees(x, y, trees)
	# If the surrounding trees is empty, then it must be on the edge
	if [] in surrounding_trees:
		return True
	for trees in surrounding_trees:
		height_differences = [surrounding_tree - tree for surrounding_tree in trees]
		if max(height_differences) < 0:
			return True
	return False

answer = 0

for x in range(0, len(trees)):
	for y in range(0, len(trees[0])):
		if is_tree_visible(x, y, trees):
			answer += 1

print(answer)