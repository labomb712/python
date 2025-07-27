l1= [1, 2, 3, 4, 5]
l2= [4, 5, 6, 7, 8]

print("리스트1:", l1)
print("리스트2:", l2)

add = sorted(list(set(l1 + l2)))
print("병합된 리스트:", add)

common= list(set(l1).intersection(set(l2)))
print("공통 요소:", common)