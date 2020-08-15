'''
Test Case 01:
5
R R R U D D
Output : 3 4

Test Case 02:
Output : 
'''
arr = int( input())
movelist = input().split()
x = 1
y = 1
move_list = ['U','D','R','L']

for s in movelist:
  if s == move_list[0]:
    x -= 1
  elif s == move_list[1]:
    x += 1
  elif s == move_list[2]:
    y += 1 
  else:
    y -= 1
  
  if x > arr or x < 1:
    x = arr if x > arr else 1

  if y > arr or y < 1:
    y = arr if y > arr else 1
    
print(x,y)