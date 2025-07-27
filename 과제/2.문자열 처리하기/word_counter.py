a=input("문장을 입력하세요:")

clean = " ".join(a.split())
count = len(clean.split())

print("공백 제거", clean)
print("단어 개수", count)