tri = sorted(map(int, input().split()))
res = tri[0] + tri[1] + min(tri[2], tri[0]+tri[1]-1)
print(res)