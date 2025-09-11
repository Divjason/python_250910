# 파이썬 지원 자료형

"""
int : 정수 // 2, 4, 6
float : 실수 // 4.2, 5.8 -> 2.0 -> 0.2 -> 0.02
bool : 논리 // True, False
str : 문자열
list : array // [1, 2, 3, 4] -> iterable -> 반복순회 기능
dict : {"first": 1}
tuple : (1, 2, 3)
"""

str1 = "Python01"
str2 = 'Python02'
bool = True
float = 10.0
int = 7
# list = ["Python01", 'Python02']
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (1, 2, 3)
set = {1, 2, 3}

print(list) #함수 => function => 기능 // Built-in Function
print(dict)

# 1.0 VS 1 VS "1"
# 1 / 3 avg => 2

# 데이터 타입 확인 함수!!
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(dict))
print(type(tuple))
print(type(set))

# 객체지향 프로그래밍 언어
# class => 메뉴얼