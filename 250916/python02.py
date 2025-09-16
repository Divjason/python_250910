# 파이썬 변수
# 파이썬 기본자료형 (숫자, 문자, 논리 등)
# 파이썬 연산자
# 파이썬 문자열 (*시퀀스형 자료구조)
# 파이썬 리스트 (*시퀀스형 자료구조)
# 파이썬 튜플 (*시퀀스형 자료구조)

# 리스트 & 튜플
# 리스트 => 유연하다 => 값 추가, 삭제
# 튜플 => 리스트와 거의 동일한 속성 및 기능 => 최초에 선언된 메모리 값을 무조건 유지

# 튜플 => 수정 x, 삭제 x => immutable
# x맨 => 돌연변이 

a = (1, 2)
b = (11, 12, ("A", "B", "C"))

print(type(b))

print(a[0], b[1])
print(a[0] + b[1])
print(a[-1] + b[-2])

# print(a.append(9))
a = (11, 12, 13)
print(type(a))

print(a[0:2])

print(a.count(11))
print(a.index(12))

# a[0] = 20

# b = list(a)
# print(b)

# print(b.append(20))
# print(b)