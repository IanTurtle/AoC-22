# A - Rock - 1 points
# B - Paper - 2 points
# C - Scissors - 3 points
# X - lose
# Y - draw
# Z - win
# win - 6 points, draw - 3 points

# Winning moves, based on what the opponent players
outcomes = {
	"A": {
		"Z": "B",
		"X": "C",
		"Y": "A"
	},
	"B": {
		"Z": "C",
		"X": "A",
		"Y": "B"
	},
	"C": {
		"Z": "A",
		"X": "B",
		"Y": "C"
	}
}

# How many points you get for choosing a move
choice_values = {
	"A": 1,
	"B": 2,
	"C": 3
}

with open("input.txt") as input:
	rounds = input.read().splitlines()

def calc_score(opponent, outcome):
	move_value = choice_values[outcomes[opponent][outcome]]
	if outcome == "X":
		return move_value 
	elif outcome == "Y":
		return move_value + 3
	else:
		return move_value + 6
		
scores = [calc_score(round.split()[0], round.split()[1]) for round in rounds]
answer = sum(scores)
print(answer)