x_array = []
y_array = []
for i in range(3):
  x, y = map(int, input().split())
  x_array.append(x)
  y_array.append(y)

for i in range(3):
  if(x_array.count(x_array[i]) == 1):
    res_x = x_array[i]
  if(y_array.count(y_array[i]) == 1):
    res_y = y_array[i]

print(res_x, res_y, end = ' ')