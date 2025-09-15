# 간단한 사칙연산 계산기 프로그래밍
# placeholder : 사용자에게 어떤 값을 받을 때, 안내메세지

num1 = float(input("첫 번째 숫자 : ")) #피연산자
operator = input("연산자를 선택해주세요. (+, -, *, /) :")
num2 = float(input("두 번째 숫자 : ")) #피연산자

if operator == "+" :
    print(f"결과 : {num1 + num2}") # f-string => formatted String
elif operator == "-" :
    print(f"결과 : {num1 - num2}")
elif operator == "*" :
    print(f"결과 : {num1 * num2}")
elif operator == "/" :
    print(f"결과 : {num1 / num2}")
else :
    print("올바른 연산자를 입력하세요!")