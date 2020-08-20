'''
Test Case 01:
3
홍길동 95
이순신 77
세종대왕 87
Output: 이순신 세종대왕 홍길동
'''

n = int(input())
arr = []
for _ in range(n):
  name, score = map(str,input().split())
  arr.append((name,score))
def setting(data):
  return data[1]
for i in sorted(arr,key = setting):
  print(i[0],end=' ')
