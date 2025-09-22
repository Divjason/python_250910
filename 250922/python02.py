# python의 대표적인 반복문

# for in
# for else
# in 반복가능한 자료형

# while
# while else
# while 문 뒤에 조건이 True여야 반복을 실행

# n = 5

# while n > 0 :
#     print(n)
#     n -= 1 # n = n - 1

# a = ["foo", "bar", "bar2"]

# while a :
#     print(a.pop())

# n = 10

# while n > 0 :
#     print(n)
#     n -= 1
#     if n == 2:
#         break
# print("Loop Ended...")

# while n > 0 :
#     n -= 1
#     print(n)
# else :
#     print("else out.")

a = ["foo", "bar", "bar2"]
s = "bar3"

i = 0

while i < len(a) :
    if a[i] == s :
        break
    i += 1
    print(i, "founding in list.")
else :
    print(s, "not found in list.")