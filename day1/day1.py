file = open("input.txt", "r")

arr = []

for line in file:
	arr.append(int(line.rstrip()))

# Part 1
def measure(arr):
	res = 0

	for i in range(len(arr) - 1):
		if arr[i+1] > arr[i]:
			res += 1

	return res

# Part 2
def measure_slider(arr):
	res = 0
	window = [arr[i] for i in range(3)]
	
	for i in range(3, len(arr)):
		prev = sum(window)
		window.pop(0)
		window.append(arr[i])
		if sum(window) > prev:
			res += 1

	return res
