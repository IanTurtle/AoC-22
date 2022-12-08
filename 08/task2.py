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

def calculate_ind_scenic_score(tree, surrounding_trees):
	scenic_score = 0
	for surrounding_tree in surrounding_trees:
		scenic_score += 1
		if surrounding_tree >= tree:
			break
	return scenic_score
	
def calculate_scenic_score(x, y, trees):
	tree = trees[x][y]
	surrounding_trees = get_surrounding_trees(x, y, trees)
	
	# Flip ordering of the left and top trees so the ordering is from the tree outwards
	surrounding_trees[0].reverse()
	surrounding_trees[2].reverse()
	
	scenic_score = 1
	for direction in surrounding_trees:
		scenic_score *= calculate_ind_scenic_score(tree, direction)

	return scenic_score

scenic_scores = []

for x in range(0, len(trees)):
	for y in range(0, len(trees[0])):
		scenic_scores.append(calculate_scenic_score(x, y, trees))

answer = max(scenic_scores)
print(answer)
