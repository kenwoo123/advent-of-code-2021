file = open("input.txt", 'r')
arr = []

for line in file:
	line = line.rstrip()
	direction, dist = line.split(" ")
	arr.append([direction, int(dist)])

def pt1(arr):
	x, y = 0, 0
	for inst in arr:
		direction, dist = inst
		if direction == 'forward':
			x += dist
		elif direction == 'up':
			y -= dist
		elif direction == 'down':
			y += dist

	return x * y

def pt2(arr):
	x, y, aim = 0, 0, 0
	for inst in arr:
		direction, dist = inst
		if direction == 'forward':
			x += dist
			y += aim * dist
		elif direction == 'up':
			aim -= dist
		elif direction == 'down':
			aim += dist

	return x * y

print(pt2(arr))