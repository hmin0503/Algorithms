"""
미로 탈출
TOO HARD
"""
#%%
from collections import deque

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if array[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if array[nx][ny] == 1:
                print(nx, ny)
                array[nx][ny] = array[x][y] + 1
                queue.append((nx,ny))
    return array[n - 1][m - 1]

print(bfs(0, 0))
# %%
