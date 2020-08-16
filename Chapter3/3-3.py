'''
Test Case 01:
3 3
3 1 2
4 1 4
2 2 2
Output : 2

Test Case 02:
2 4
7 3 1 8
3 3 3 4
Output: 3
'''
n, m= map( int, input().split())
mom = 0;
for i in range(0,n):
  arr = list(map(int, input().split()))
  if mom < min(arr):
    mom = min(arr)

print(mom);