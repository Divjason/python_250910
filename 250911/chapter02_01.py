# 연산자

"""
+
-
*
/

%
//
abs(x)
pow(x, y) x**y => pow(2, 3) 2**3
"""

i1 = 39
i2 = 939
i3 = 1

f1 = 1.234
f2 = 3.939
f3 = 1.0

print("i1 + i2 :", i1 + i2)
print("f1 + f2 :", f1 + f2)
print("i3 + f3 :", i3 + f3)

# 자동 형변환 : 실수 + 정수 => 실수

a = 3.
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))

# 형태 => 연산처리 오류 여부 판단
# 수동 형변환
# truthy falsy => 0 // 1 => 2진수 => 0, 1

print(float(b))
print(int(a))
print(int(True))
print(int(False))
print(complex(b))

print(pow(2, 3))
print(6 / 4)
print(6 % 4) # 짝수, 홀수

# a + bj : 

