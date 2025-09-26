# 예외처리
# 프로그래밍 영역 : 
# 1) 초중급 단계 : 반복문 * 리스트 잘 사용하는 사람
# 2) 중급 단계 : 예외 처리 잘 하는 사람

try :
    n = int(input("Enter a number : "))
    print(f"ok! Your number is : {n}")
except ValueError :
    print("This is not a number")