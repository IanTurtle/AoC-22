import io

answer = 14
with open("input.txt", "rb") as input:
	fi = io.FileIO(input.fileno())
	fb = io.BufferedReader(fi)
	# Read in the first 4 characters
	check = fb.read(14)
	
	while char := fb.read(1):		
		if len(check) > len(set(check)):
			check = check[1:] + char
			answer += 1
		else:
			break
		
print(answer)