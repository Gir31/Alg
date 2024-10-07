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

def dist(a, b):
	d = 1#???


def dist_sq(a, b):
	d = 1#???

def brute_force(arr, i1, i2):
	md = ???
	for x: # i1 ~ 12
		for ??: #x+1 ~ i2
			if d < md:
				md = d
				s = 
				e =

	return s, e, d


def dnc(arr, i1, i2):
	switch size:
		<= 1: return -1, -1, 0
		== 2: return i1, i2, dist(i1, i2)
		== 3: return brute_force(arr, i1, i2)
	
	# size >= 4
	s1, e1, d1 = dnc(...)
	s2, e2, d2 = dnc(...)

	if d1 < d2:
		??
	else:
		???

	d 결정

	x좌표: 중간점x좌표-d ~ 중간점 x좌표+d
	index1: x좌표가 중간점x좌표-d 이상인 점들 중 가장 왼쪽 index
	index2: x좌표가 중간점x좌표+d 이하인 점들 중 가장 오른쪽 index
	strip = [t for t in y_sorted if t[2] >= index1 and t[2] <= index2]




print(coords)
coords.sort(key=lambda t:t[0])

x_sorted = [(coords[i][0], coords[i][1], i) for i in range(len(coords))]

y_sorted = sorted(x_sorted, key=lambda t:t[1])

x_sorted = sorted(coords, ....)

#s, e, d = brute_force(coord, 0, len(coords) - 1)
s, e, d = dnc(coords, 0, len(coords) - 1)


#print(f'{s=} {e=} {d=}')

print(f'[{s}]{coords[s]} - [{e}]{coords[e]}, {d=}')