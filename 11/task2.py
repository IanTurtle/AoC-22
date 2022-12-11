import re
import math

with open("input.txt") as input:
	lines = input.read().splitlines()

class Monkey():
	
	def __init__(self, items, operation, test_val, if_true, if_false):
		self.items = items
		self.operation = operation.split()
		self.test_val = test_val
		self.if_true = if_true
		self.if_false = if_false
		self.inspected = 0
	
	def evaluate(self, item):
		nums = [item if x == "old" else int(x) for x in [self.operation[0], self.operation[2]]]
		new = 0
		match self.operation[1]:
			case "+":
				new = int(sum(nums))
			case "*":
				new = int(math.prod(nums))
			case _:
				pass
		return new, (new%self.test_val == 0)
			
	def throw(self):
		throws = []
		while self.items:
			self.inspected += 1
			item = self.items.pop(0)
			new, evaluation = self.evaluate(item)
			if evaluation: 
				throws.append([new, self.if_true])
			else:
				throws.append([new, self.if_false])
		return throws
	
	def catch(self, item):
		self.items.append(item)
		
	def __str__(self):
		return str(self.items)
	
	def __repr__(self):
		return str(self.items)

def parse_input():
	modulo = 1
	monkeys = []
	for i in range(0, len(lines), 7):
		monkey = lines[i:i+7]
		starting_items_pattern = re.compile(r"  Starting items: (.*)")
		operation_pattern = re.compile(r"  Operation: new = (.*)")
		test_pattern = re.compile(r"  Test: divisible by (\d*)")		
		true_pattern = re.compile(r"    If true: throw to monkey (\d*)")
		false_pattern = re.compile(r"    If false: throw to monkey (\d*)")
		
		
		items = [ int(x) for x in starting_items_pattern.search(monkey[1]).group(1).split(", ")]
		operation = operation_pattern.search(monkey[2]).group(1)
		test = int(test_pattern.search(monkey[3]).group(1))
		if_true = int(true_pattern.search(monkey[4]).group(1))
		if_false = int(false_pattern.search(monkey[5]).group(1))
		monkeys.append(Monkey(items, operation, test, if_true, if_false))
		modulo *= test
	return monkeys, modulo

monkeys, modulo = parse_input()
for i in range(0, 10000):
	for monkey in monkeys:
		for worry, target in monkey.throw():
			monkeys[target].catch(worry%modulo)

monkeys_sorted = sorted(monkeys, key=lambda x:x.inspected, reverse=True)

answer = monkeys_sorted[0].inspected * monkeys_sorted[1].inspected
print(answer)
