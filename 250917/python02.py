"""
1. 변수
2. 자료형(기본)
3. 연산자
4. 문자열
5. 튜플
6. 리스트
7. 딕셔너리
8. set (*집합) : Numpy, Scipy => 중복해서 값을 사용할 수 없다, 순서x
9. 조건문
10. 반복문
11. class
"""

# a = list()
# b = int()
# c = tuple()
# b = float()
# d = dict()

# e = set()
# print(type(e))

# f = set([1, 2])
# print(f)

# # [] : 리스트
# # () : 튜플
# # {} : 딕셔너리 (*키 : 밸류 => 속성)
# # {} : 튜플 혹은 리스트 단일값 => set

# v = {1, 2, 2, 4}
# print(dir(v))

# print(2 in v)

# z = tuple(v)

# print(z[0:1]) # set 슬라이싱 기능!!

# print(len(v))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = {9, 8, 7}

# print(type(s1), type(s2), type(s3))

print(f"s1 & s2 : {s1 & s2}") # 서로다른 set 집합의 교집합 결과 도출
print(f"s1 & s2 : {s1.intersection(s2)}") # 서로다른 set 집합의 교집합 결과 도출

print(f"s1 | s2 : {s1 | s2}")
print(f"s1 | s2 : {s1.union(s2)}")

print(f"s1 - s2 : {s1 - s2}")
print(f"s1 - s2 : {s1.difference(s2)}")

# 서로 다른 두 개의 집합 자료형의 교집합 원소가 존재하는지 여부 판단 함수
print(f"s1 & s3 : {s1.isdisjoint(s3)}")

# 교집합 / 합집합 / 차집합 / 부분집합

print(s1.issubset(s2))
print(s3.issubset(s2))
print(s2.issuperset(s3))

