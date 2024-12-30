triangle = []
for i in range(3):
  n = int(input())
  triangle.append(n)

if (sum(triangle) != 180):
  print("Error")
elif (triangle[0] == triangle[1] == triangle[2]):
  print("Equilateral")
elif ((triangle[0] != triangle[1]) and (triangle[1] != triangle[2]) and (triangle[0] != triangle[2])):
  print("Scalene")
else:
  print("Isosceles")