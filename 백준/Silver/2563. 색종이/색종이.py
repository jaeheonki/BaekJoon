n = int(input())
array = [[0]*100 for i in range(100)]
count = 0

for i in range(n):
  x, y = map(int, input().split())
  for j in range(x, x+10):
    for k in range(y, y+10):
      array[j][k] = 1

for i in range(100):
  count += sum(array[i])
  
print(count)