coords = [
	(620, 332), (784, 623), (182, 555), (1413, 451), (1092, 660), 
	(30, 217), (525, 148), (1311, 887), (1228, 353), (54, 68), 
	(1155, 838), (467, 563), (86, 535), (32, 630), (739, 766), 
	(1386, 16), (1565, 828), (868, 264), (1301, 786), (883, 415), 
	(479, 534), (1101, 35), (671, 405), (1478, 230), (1343, 834), 
	(647, 97), (972, 447), (327, 334), (716, 151), (233, 411), 
	(486, 431), (1017, 381), (329, 830), (1286, 739), (1528, 248), 
	(216, 294), (1306, 540), (204, 715), (77, 120), (97, 178), 
	(809, 28), (354, 205), (123, 551), (248, 828), (888, 139), 
	(594, 494), (576, 702), (64, 218)
]

coords.sort(key=lambda t:t[0])
x_sorted = [(coords[i][0], coords[i][1], i) for i in range(len(coords))]
y_sorted = sorted(x_sorted, key=lambda t:t[1])

def dist(a, b): 
	x1, y1 = a
	x2, y2 = b
	return (x1 - x2)**2 + (y1 - y2)**2

def brute_force(arr, coord1, coord2):

	s, e = coord1, coord2
	md = dist(arr[coord1], arr[coord2])
	
	for start in range(coord1, coord2 + 1):
		for end in range(start + 1, coord2 + 1):
			d = dist(arr[start], arr[end])
			if d < md:
				md = d
				s = start
				e = end
	return s, e, md


def dnc(arr, i1, i2):
	size = i2 - i1 + 1

	if size == 1: 
		return -1, -1, 0
	elif size == 2: 
		return i1, i2, dist(arr[i1], arr[i2])
	elif size == 3: 
		s, e, d = brute_force(arr, i1, i2)
		return s, e, d
	
	mid_index = size // 2 + i1 - 1

	s1, e1, d1 = dnc(arr, i1, mid_index)
	s2, e2, d2 = dnc(arr, mid_index + 1, i2)

	if d1 < d2:
		return s1, e1, d1
	else:
		return s2, e2, d2

def dnc_all(arr, i1, i2):
	s, e, d = dnc(arr, i1, i2)

	mid_index = (i2 + i1)//2 - 1
	left_index, right_index = i1, i2

	for i in range(mid_index, i1, -1):
		ld = (arr[mid_index][0] - arr[i][0])**2
		if ld <= d: left_index = i
		else: break

	for i in range(mid_index, i2, 1):
		rd = (arr[mid_index][0] - arr[i][0])**2
		if rd <= d: right_index = i
		else: break

	strip = [t for t in y_sorted if t[2] >= left_index and t[2] <= right_index]

	for i in range(len(strip)):
		for j in range(i + 1, len(strip)):
			dis = dist(arr[i], arr[j])
			if dis < d:
				s, e, d = i, j, dis
			else:
				break

		

	return s, e, d

s, e, d = dnc_all(coords, 0, len(coords) - 1)

print(f'[{s}]{coords[s]} - [{e}]{coords[e]}, {d=}')