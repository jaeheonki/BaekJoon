n = int(input())
x_array = []
y_array = []

for i in range(n):
  x, y = map(int, input().split())
  x_array.append(x)
  y_array.append(y)

if n <= 1:
  print(0)
else:
  print((max(x_array) - min(x_array)) * (max(y_array) - min(y_array)))