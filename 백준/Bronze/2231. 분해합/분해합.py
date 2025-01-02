n = int(input())
res = 0

for i in range(n):
  temp = i
  sum = i
  while temp > 0:
    sum += temp % 10
    temp //= 10
  if sum == n:
    res = i
    print(res)
    break

if res == 0:
  print(0)