try:
    dan = int(input("몇 단을 출력할까요? "))
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")
else:
    print(f"{dan}단 구구단:")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")