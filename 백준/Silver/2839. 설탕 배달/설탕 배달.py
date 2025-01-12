n = int(input())

cnt_array = []
for i in range((n // 5) + 1):
  if (((n - (i * 5)) % 3) == 0):
    cnt_array.append(i + ((n - (i * 5)) // 3))

if(len(cnt_array) != 0):
  print(min(cnt_array))
else:
  print(-1)