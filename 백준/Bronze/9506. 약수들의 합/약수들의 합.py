while True :
  n = int(input())
  if n == -1 :
    break
  sent = str(n) + " = "
  sum = 0
  for i in range(1, (n//2 + 1)):
    if n % i == 0:
      sent +=  str(i) + " + "
      sum += i
  if sum == n:
    sent = sent.rstrip(" + ")
    print(sent)
  else :
    print(str(n) + " is NOT perfect.")