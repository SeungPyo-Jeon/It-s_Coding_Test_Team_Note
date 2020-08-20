'''
Test Case 01:
5 3
1 2 5 4 3
5 5 6 6 5
Output: 26
'''

n,k = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1.sort(reverse=False)
arr2.sort(reverse=True)

for i in range(k):
  arr1[i] = arr2[i]
a = 0 
for i in arr1 :
  a += i
print(a)
