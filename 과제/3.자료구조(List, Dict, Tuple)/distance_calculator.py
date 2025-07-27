import math

p1 = (0, 0)
p2 = (3, 4)


print(f"점1: {p1}")
print(f"점2: {p2}")

d= math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print(f"두 점 사이의 거리: {d}")