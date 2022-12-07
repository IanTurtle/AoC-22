import re

class File():
		
	def __init__(self, name, size, parent_dir):
		self.size = size
		self.name = name
		self.parent_dir = parent_dir
		if not parent_dir:
			self.full_path = "/"
		elif self.parent_dir.full_path == "/":
			self.full_path = f"/{name}"
		else:
			self.full_path = f"{parent_dir.full_path}/{name}"
		
	def __str__(self):
		return f"{self.name} {self.size}"

	def __repr__(self): 
		return f"{self.name} {self.size}"
		
class Dir(File):
	
	# Directories are empty by default
	def __init__(self, name="", parent_dir=None):
		self.files = []
		File.__init__(self, name, 0, parent_dir)
		
	def update_size(self, size):
		self.size += size
		if self.parent_dir:
			self.parent_dir.update_size(size)
	
	def add_file(self, name, size):
		f = File(name, size, self)
		self.update_size(size)
		self.files.append(f)
		return f
	
	def add_dir(self, name):
		d = Dir(name, self)
		self.files.append(d)
	
	def get_file(self, name):
		matching = [ file for file in self.files if file.name == name ]
		if matching:
			return matching[0]
		else:
			return None
			
	def find_directories_less_than_size(self, size, matching = []):
		dirs = [file for file in self.files if isinstance(file, Dir)]
		for dir in dirs:
			if dir.size < size:
				matching = [dir] + dir.find_directories_less_than_size(size, matching)
			else:
				matching = dir.find_directories_less_than_size(size, matching)
		return matching
	
	def __str__(self):
		return f"{self.name} {self.size}"
		
	def __repr__(self): 
		return f"{self.name} {self.size}"

with open("input.txt") as input:
	lines = input.read().splitlines()

root = Dir("/")
current_dir = root

for line in lines:
	cd_pattern = re.compile(r"\$ cd (.*)")
	dir_pattern = re.compile(r"dir (.*)")
	file_pattern = re.compile(r"(\d+) (.*)")
	if result := cd_pattern.search(line):
		dir = result.group(1)
		if dir == "/":
			pass
		elif dir == "..":
			current_dir = current_dir.parent_dir
		else:
			current_dir = current_dir.get_file(dir)
			
	elif result:= dir_pattern.search(line):
		dir = result.group(1)
		current_dir.add_dir(dir)
	elif result:= file_pattern.search(line):
		size = int(result.group(1))
		file = result.group(2)
		current_dir.add_file(file, size)

answer = 0
for dir in root.find_directories_less_than_size(100000):
	answer += dir.size
print(answer)
