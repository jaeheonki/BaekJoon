arr = []
max = 0
max_i, max_j = 0, 0
for i in range(9):
  arr.append(list(map(int, input().split())))

for i in range(9):
  for j in range(9):
    if arr[i][j] > max :
      max = arr[i][j]
      max_i, max_j = i, j

print(max)
print(max_i + 1, max_j + 1, end = ' ')
