x, y, w, h = map(int, input().split())
i, j = 0 , 0
if x >= w / 2:
  i = w - x
else:
  i = x

if y >= h / 2 :
  j = h - y
else:
  j = y

print(i if i < j else j)
