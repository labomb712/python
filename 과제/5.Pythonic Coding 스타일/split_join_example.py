
text = "Python is awesome programming language"

print(f"원본 문자열: {text}")

words = text.split(' ')
print(f"분리된 단어들: {words}")


hyphen_joined_text = "-".join(words)
print(f"하이픈으로 연결: {hyphen_joined_text}")


uppercase_words = [word.upper() for word in words]

space_joined_uppercase_text = " ".join(uppercase_words)
print(f"대문자로 변환 후 공백으로 연결: {space_joined_uppercase_text}")