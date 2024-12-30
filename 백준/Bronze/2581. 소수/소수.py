m = int(input())
n = int(input())

prime_list = []

for i in range(m, n+1):
  if i>1 :
    for j in range(2, i):
      if(i % j == 0):
        break
    else:
      prime_list.append(i)  
if(prime_list == []):
  print(-1)
else:
  print(sum(prime_list))
  print(min(prime_list))

