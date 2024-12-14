num, b = map(int,input().split())
res = []
while num > 0:
  rem = num % b
  if rem >= 10:
    rem = chr(rem+55)
  res.append(rem)
  num = num // b

for i in reversed(res):
  print(i, end = '') 