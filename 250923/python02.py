# 중첩 : 
# if조건문의 중첩
# for 반복문의 중첩

# if True :
#     if True :

# for x in range(10) :
#     for y in range(10) :

def arg() :
    return 100

def nested_func(num) :
    def func_in_func(num) :
        return num
    print("In func")
    return func_in_func(num + 100)

test = nested_func(arg())

print(test)

# 객체지향 언어!!
# 1급 시민 => 3가지 조건 충족
# 1) 함수 => 또 다른 함수의 인자값으로 사용될 수 있어야함
# 2) 함수 => 또 다른 함수의 반환값으로 사용될 수 있어야함
# 3) 함수 => 변수 안에 담길 수 있어야함

# 파이썬이라는 언어의 문법의 유연함!!

# 2가지 부류 : 

# 백엔드 기반 서버구현 + 풀스택 개발
# 데이터를 수집.저장.전처리 빅데이터 기반 데이터 분석가, 엔지니어, AI 개발자
