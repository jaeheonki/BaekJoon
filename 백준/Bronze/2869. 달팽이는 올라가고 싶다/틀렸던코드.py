#처음에 반복문을 사용하였으나 시간 초과로 틀렸다ㅠㅠ
a, b , v = map(int, input().split())
height = 0
days = 0
while True:
  days = days + 1
  height = height + a
  if height >= v:
    break
  height = height - b
print(days)

