# A,X - Rock - 1 points
# B,Y - Paper - 2 points
# C,Z - Scissors - 3 points
# win - 6 points, draw - 3 points

# Winning moves, based on what the opponent players
outcomes = {
	"A": {
		"win": "Y",
		"draw": "X"
	},
	"B": {
		"win": "Z",
		"draw": "Y"
	},
	"C": {
		"win": "X",
		"draw": "Z"
	}
}

# How many points you get for choosing a move
choice_values = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

with open("input.txt") as input:
	rounds = input.read().splitlines()

def calc_score(opponent, player):
	base = choice_values[player]
	if outcomes[opponent]["draw"] == player:
		return base + 3
	elif outcomes[opponent]["win"] == player:
		return base + 6
	else:
		return base + 0
		
scores = [calc_score(round.split()[0], round.split()[1]) for round in rounds]
answer = sum(scores)
print(answer)