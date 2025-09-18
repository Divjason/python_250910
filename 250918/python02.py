# 반복문 => 어떤 프로그래밍 언어 "항상 중요함!"
# 프로그래밍 영역 => 반복문 위대
# 프로그래밍 장점 극대화 => 인간이 따라할 수 있는 무한한 반복
# 반복횟수가 아무리 많아도 굉장히 빠른시간 안에 해결!

# 반복 => 자료구조 "iterable"
# 자료를 반복해서 사용하려면 => 자료형 // 변수...

# items = [1, 2, 3, 4, 5]
# sum = 0

# for item in items :
#     sum += item # 0 + 1 + 2 + 3 + 4 + 5

# # sum = 10
# print(sum)

# for()
# forEach()
# for of
# for in

# range() # => 1차원의 리스트 (*배열) 값을 생성 // 2차원 리스트
# [1, 2, 3, 4, 5] -> [[1, 2], [3, 4]]

# for v1 in range(10) :
#     print(v1)

# names = ["David", "Dave", "Jane"]

# for index, name in enumerate(names) :
#     print(f"{index + 1}등 : {name}")

# 타입 : enum : 어떠한 형태의 자료던지 간에 카운트로 셈할 수 있도록 자료형

# for v2 in range(1, 11) : # 인자값이 1개면 갯수 // 인자값이 2개면 
#     print(v2)

# for v3 in range(1, 11, 2) : # 인자값이 1개면 갯수 // 인자값이 2개면 
#     print(v3)

# sum = 0

# for v4 in range(1, 1001) :
#     # sum = sum + v4
#     sum += v4 # 복합대입연산자

# print(sum)

# sum() => 인자값을 모두 순차적으로 더해주는 역할 : 누산기

# testSum = sum(range(1, 1001)) # 집계함수

# print(sum(range(1, 1001)))


# word = "Beautiful"
# # print(dir(word))

# for s in word :
#     print(s)

my_info = {
    "name": "David",
    "age": 20,
    "city": "seoul"
}

# print(my_info["name"])

# print(dir(my_info))

# for k in my_info :
#     print(f"{k} : {my_info[k]}")

for k in my_info :
    print(f"{k} : {my_info.get(k)}")