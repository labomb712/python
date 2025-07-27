
def greet(name, lang="ko", message="안녕하세요"):
    if lang == "ko":
        print(f"{message}, {name}님!")
    elif lang == "en":
        print(f"Hello, {name}!")
    else:
        print("지원하지 않는 언어입니다.")

greet("김철수")

greet("John", lang="en")

greet("이영희", lang="ko", message="안녕하세요, 좋은 하루 되세요")