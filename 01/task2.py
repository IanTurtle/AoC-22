with open("input.txt") as input:
	calories = input.read().splitlines()
	
totals = []
elfTotal = 0
for value in calories:
	try:
		elfTotal += int(value)
	except ValueError:
		totals.append(elfTotal)
		elfTotal = 0
totals.append(elfTotal)

one = max(totals)
totals.remove(one)
two = max(totals)
totals.remove(two)
three = max(totals)

answer = one + two + three
print(answer)