t = int(input())
tests = []
coins= [25, 10, 5, 1]
c_res = []
for i in range(t):
  tests.append(int(input()))
  for coin in coins:
    c_res.append(tests[i] // coin)
    tests[i] = tests[i] % coin
for i, element in enumerate(c_res, start = 1):
  if i%4 == 0:
    print(element)
  else:
    print(element, end = ' ')