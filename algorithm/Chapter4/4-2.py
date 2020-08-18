'''
Test Case 01:
a1
Output : 2
'''
n = str(input())
r = ['a','b','c','d','e','f','g','h']
y = int(n[-1])
x = 0
for i in range(0,len(r)):
  if n[0] == r[i]:
    x = i+1
count = 0

def isIn( x , y):
  if x > 0 and x < 9:
    if y > 0 and y < 9:
      return 1
  return 0
  
xlist = [x-1,x+1,x-1,x+1,x-2,x-2,x+2,x+2]
ylist = [y-2,y-2,y+2,y+2,y-1,y+1,y-1,y+1]

for i in range(len(xlist)):
  count += isIn(xlist[i],ylist[i])

print(count)
