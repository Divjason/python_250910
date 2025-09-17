a = {
    "name": "Park",
    "phone": "01012345678",
    "birth": "001231"
}

# a["address"] = "Seoul"
# a["name"] = "Peter"

# print(a, len(a))

# print(dir(a)) # 변수이던지 간에 dir() => 해당 변수의 세부 속성값 확인! => __iter__
# # 반복 순회할 수 있는 시퀀스 자료형 속성을 상속받은 자료구조를 담고 있는 변수
# # iterable => 반복할 수 있는
# # iterator

# b = [1, 2, 3, 4]
# print(dir(b))

# c = "happy birthday"
# print(dir(c))

# d = (5, 6, 7, 8)
# print(dir(d))

# print(a.keys())

# for key_items in a.keys() :
#     print(key_items)

# print(a.values())

# print(a.items())

# for tuple_items in a.items() :
#     print(tuple_items[1])

# print(dir(a))

# first = a.pop("name") # pop 함수 내부 "인수 | 인자값"

# last = a.popitem() # 딕셔너리 자료구조에서 맨마지막번째 값을 잘라내기

# print(a, last)

# in => ~안, 내부 => 논리형 값을 반환

test_keyword = "name"

print(test_keyword in a)

del a["name"]
print(a)

# 딕셔너리 내부 값을 제거하는 3가지 방법
# pop(인자값), popitem(), del
# 어떤게 x
# 1개의 결과 도출 => 수만가지 방법 찾아