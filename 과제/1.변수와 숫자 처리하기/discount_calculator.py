a=int(input("상품 가격을 입력하세요:"))
b=int(input("할인율을 입력하세요(%):"))
print("원래가격:",a)
print("할인율:",b)

x = a*(b/100)
z = a-x

print("할인금액: ",x)
print("최종가격: ",z)
