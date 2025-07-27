try:
    num = int(input("숫자를 입력하세요: "))
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")
else:
    # 1은 소수가 아님
    if num < 2:
        print(f"{num}은(는) 소수가 아닙니다.")
    # 2는 유일한 짝수 소수
    elif num == 2:
        print(f"{num}은(는) 소수입니다.")
    # 2를 제외한 짝수는 소수가 아님
    elif num % 2 == 0:
        print(f"{num}은(는) 소수가 아닙니다.")
    else:
        # 3부터 num의 제곱근까지 홀수로 나누어 떨어지는지 확인
        # num의 제곱근까지만 확인해도 되는 이유는, num이 n*m일 때
        # n이나 m 중 적어도 하나는 num의 제곱근보다 작거나 같기 때문입니다.
        is_prime = True
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(f"{num}은(는) 소수입니다.")
        else:
            print(f"{num}은(는) 소수가 아닙니다.")