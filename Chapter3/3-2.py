'''
Test Case 01:
5 8 3
2 4 5 4 6
Output : 46
'''
n, m, k = map( int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
count = 0

for i in range(0,m):
  if (i+1) % k == 0:
    count += arr[1]
  else:
    count += arr[0]  
  
print(count);