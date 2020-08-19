'''
Test case 01:
5 6
101010
111111
000001
111111
111111
Output: 10
'''
from collections import deque

n, m = map(int,input().split())
maps = []

for i in range(n):
  maps.append( list(map(int,input())) )

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if maps[nx][ny] == 0:
        continue
      if maps[nx][ny] == 1:
        maps[nx][ny] += maps[x][y]
        queue.append((nx,ny))

  return maps[n-1][m-1]

result = BFS( 0, 0)
   
print(result)
