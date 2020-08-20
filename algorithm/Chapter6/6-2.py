'''
Test Case 01:
3
15
27
12
Output: 27 15 12
'''

n = int(input())
arr = []
for _ in range(n):
  arr.append(input())
for i in sorted(arr,reverse=True):
  print(i,end=' ')
