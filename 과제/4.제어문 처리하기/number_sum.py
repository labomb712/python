total_sum = 0

while True:
    try:
        num = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))

        if num == 0:
            break
        
        total_sum += num
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")

print(f"입력된 숫자들의 합: {total_sum}")