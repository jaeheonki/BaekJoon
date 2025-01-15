import sys
n = int(input())

st_array = []
cnt = -1

for _ in range(n):
  words = sys.stdin.readline().rstrip()
  if "push" in words:
    num = int(words.replace("push", "").strip())
    cnt += 1
    st_array.append(num)
  elif words == "pop":
    if cnt == -1:
      print(-1)
    else:
      print(st_array[-1])
      st_array.pop()
      cnt -= 1
  elif words == "size":
    print(cnt + 1)
  elif words == "empty":
    if cnt == -1:
      print(1)
    else:
      print(0)
  elif words == "top":
    if cnt == -1:
      print(-1)
    else:
      print(st_array[cnt])
