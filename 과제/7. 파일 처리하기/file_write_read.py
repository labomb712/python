
lines_to_write = [
    "안녕하세요",
    "파이썬 파일 처리를 연습하고 있습니다",
    "오늘은 좋은 날씨입니다"
]

file_name = "example.txt"

print("파일에 저장할 내용:")
for line in lines_to_write:
    print(line)

with open(file_name, 'w', encoding='utf-8') as file:
    for line in lines_to_write:
        file.write(line + '\n')
print("\n파일에서 읽어온 내용:")


with open(file_name, 'r', encoding='utf-8') as file:
    read_content = file.read()
    print(read_content)