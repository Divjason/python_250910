# 람다식
# 함수는 기본적으로 선언부 & 호출부
# 함수를 선언한 다음, 호출을 하게되면 기본적으로 함수는 객체를 생성하게 되어있음
# 로컬 컴퓨터의 메모리 (리소스) 할당하게 됨
# 람다식 => 함수 실행 => heap 메모리공간에 바로 함수 실행 => 종료 => 메모리 초기화
# 람다식이 너무 남발될 때, 구문에 대한 정확 이해도 낮아짐
# 1회성으로 함수를 만들어서 실행하고 종료해도 되는 경우!

# 전통적인 함수구문
# def mul_func(x, y) :
#     return x * y

# 람다식 = 익명함수을 활용한 함수실행
# key = lambda x, y : x * y

def mul_func(x, y) :
    return x * y

print(mul_func(10, 50))

mul_func_var = mul_func

print(mul_func_var(20, 50))

lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))

print("----")

def func_final(x, y, func) :
    print(x * y * func(100, 200))

func_final(10, 20, lambda x, y: x * y)