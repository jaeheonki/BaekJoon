num, b = input().split()
num = list(num)
sum = 0
b = int(b)
for i in range(len(num)):
  if 'A' <= num[-(i+1)] <= 'Z':
    num[-(i+1)] = ord(num[-(i+1)]) - 55
  else:
    num[-(i+1)] = int((num[-(i+1)]))
  sum += num[-(i+1)] * (b ** i)
print(sum)