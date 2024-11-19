d = [2,5,9,3,7,2,9,3,8,2,3]

mc = len(d) - 1

INF = float('inf')

C = [[0 for _ in range(mc + 1)] for _ in range(mc + 1)] #곱셈 횟수 저장하는 이차원 배열
P = [[0 for _ in range(mc + 1)] for _ in range(mc + 1)] #몇번째 행렬 뒤에서 해야하는가 이차원 배열

for sps in range(2, mc + 1):
	spc = mc - sps + 1 #sub problem count
	for beg in range(1, spc + 1):
		end = beg + sps - 1 # sps = 3, beg = 4, end = 6
		candidate = INF, beg
		for k in range(beg, end):
			t = C[beg][k] + C[k+1][end] + d[beg-1] * d[k] * d[end] # (?1x?2)행렬과 (?2x?3) 행렬을 곱할때의 산술 곱셈 수
			if candidate[0] > t:
				candidate = t, k
			#최소값 갱신

		C[beg][end] = candidate[0]
		P[beg][end] = candidate[1]


def path(i, j):
	if P[i][j] == i:
		return f'A{i}'

	a = path(i, P[i][j])
	b = path(P[i][j], j)

	return f'({a}x{b})'


print(f'{path(1, mc)}, {C[1][mc]}')