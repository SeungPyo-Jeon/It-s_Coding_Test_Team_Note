'''
Test Case 01:
25 5
Output : 2

Test Case 02:
25 3
Output : 6
'''
n, k= map( int, input().split())
count = 0;

while n >= k:
  while n % k != 0:
    n -= 1
    count += 1
  n //= k
  count += 1

while n != 1:
  n -= 1
  count += 1

print(count)
