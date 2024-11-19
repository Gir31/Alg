edges=[
    (0, 2, 267), (0, 10, 292), (0, 14, 162), (0, 17, 311), (0, 23, 281), 
    (1, 11, 331), (1, 19, 307), (1, 22, 395), (2, 6, 256), (2, 10, 319), 
    (2, 14, 111), (2, 16, 316), (2, 18, 405), (2, 20, 451), (2, 21, 415), 
    (2, 24, 488), (3, 8, 249), (3, 12, 438), (3, 15, 84), (4, 7, 445), 
    (4, 10, 53), (4, 16, 320), (4, 17, 135), (4, 20, 229), (4, 24, 298), 
    (5, 9, 367), (5, 13, 483), (5, 15, 261), (5, 19, 358), (6, 7, 109), 
    (6, 12, 358), (6, 14, 319), (6, 16, 456), (6, 18, 153), (6, 21, 465), 
    (7, 12, 440), (7, 13, 465), (7, 14, 210), (7, 23, 236), (8, 9, 106), 
    (10, 16, 285), (11, 13, 371), (11, 19, 53), (12, 13, 243), (12, 18, 364), 
    (12, 21, 395), (12, 22, 442), (13, 21, 170), (14, 18, 451), (14, 23, 318),
    (16, 17, 287), (16, 23, 325), (17, 24, 392), (19, 22, 146), (20, 24, 76)
]
num_vertex = 25

INF = float('inf')

D = [[0 for _ in range(num_vertex)] for _ in range(num_vertex)] # 출발지 목적지 이차원 배열
P = [[0 for _ in range(num_vertex)] for _ in range(num_vertex)]

for i in range(num_vertex):
    for j in range(num_vertex):
        if i != j:
            D[i][j] = INF


for i, j, w in edges:
    D[i][j] = w
    D[j][i] = w


for k in range(num_vertex):
    for i in range(num_vertex):
        for j in range(num_vertex):
            dist = D[i][j]
            via = D[i][k] + D[k][j]
            if via < dist:
                D[i][j] = via
                P[i][j] = k

def path(i, j):
    if P[i][j] != 0:
        pik = path(i, P[i][j])
        pkj = path(P[i][j], j)
        return f'{pik}{pkj}'
    return f'->{j}'

for i in range(num_vertex):
    for j in range(i + 1, num_vertex):
        p = path(i, j)
        print(f'{i}{p} ({D[i][j]})')


