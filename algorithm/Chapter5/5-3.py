'''
Test case 01:
4 5
00110
00011
11111
00000
Output: 3

Test case 02:
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
Output: 8
'''

n, m = map(int,input().split())
ices = []
for i in range(n):
  ices.append( list(map(int,input())) )

def DFS(x,y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return 0
  if ices[x][y] == 0:
    ices[x][y] = 1
    DFS(x-1,y)
    DFS(x+1,y)
    DFS(x,y-1)
    DFS(x,y+1)
    return 1 
  return 0

result = 0;
for i in range(n):
  for j in range(m):
    result += DFS(i,j)

print(result)
