with open("input.txt") as input:
	commands = [ command for command in input.read().splitlines()]

commands.reverse()

register = 1
answer = 0
cycle = 0
cycles_left = 0
pixels = []

while True:
	cycle += 1
	sprite_range = [ register-1, register, register+1 ]
	if not cycles_left:
		if commands:
			command = commands.pop()
		else:
			break
	operation = command.split()[0]
	if (cycle-1)%40 in sprite_range:
		pixels.append("#")
	else:
		pixels.append(".")
	match operation:
		case "noop":
			cycles_left = 1
		case addx:
			if not cycles_left:
				cycles_left = 2
			if cycles_left == 1:
				register += int(command.split()[1])
	cycles_left -= 1	
	

for i in range(0, len(pixels), 40):
    print("".join(pixels[i:i+40]))