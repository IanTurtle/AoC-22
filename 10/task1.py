with open("input.txt") as input:
	commands = [ command for command in input.read().splitlines()]

commands.reverse()

register = 1
answer = 0
cycle = 0
cycles_left = 0

while True:
	cycle += 1
	if not cycles_left:
		if commands:
			command = commands.pop()
		else:
			break
	operation = command.split()[0]	
	if (cycle-20)%40 == 0:
		answer += (cycle * register)
	match operation:
		case "noop":
			cycles_left = 1
		case addx:
			if not cycles_left:
				cycles_left = 2
			if cycles_left == 1:
				register += int(command.split()[1])
	cycles_left -= 1	
print(answer)