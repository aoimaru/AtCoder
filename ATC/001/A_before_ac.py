
import sys
sys.setrecursionlimit(1000000)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x, y):
	land_judge[x][y] = 1
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx and nx < H and 0 <= ny and ny < W and land_judge[nx][ny] == 0 and land[nx][ny] != "#":
			dfs(nx, ny)

H,W = map(int,input().split())
land = [list(input()) for i in range(H)]
land_judge = [[0] * W for i in range(H)]

for i in range(H):
	for j in range(W):
		if land[i][j] == "s":
			dfs(i,j)
			

judge = "No"
for i in range(H):
	for j in range(W):
		if land[i][j] == "g" and land_judge[i][j]:
			judge = "Yes"
print(judge)