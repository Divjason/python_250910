nums = [14, 3, 4, 7, 10, 24, 17, 2, 34, 15, 14, 36, 38]

# print(type(num), dir(num))
# 무한루프 => 반복문의 종료가 존재 X
# 컴퓨터의 메모리 과부하 야기
# 기저조건 : 특정 조건 => 종료!! => 재귀적 알고리즘

# for num in nums :
#     if num == 34 :
#         continue
#         print("found : 34!")
#         # break
#     else :
#         print("Not found: ", num)

# lt = ["1", 2, 5, True, 4.3]

# for item in lt :
#     if type(item) is bool :
#         continue
#     print("Current Type : ", type(item))

# for num in nums :
#     if num == 3 :
#         print("found : 3")
#         break
#     else :
#         print("found :", num)

# for num in nums :
#     if num == 3 :
#         print("found : 3")
#         break
# else :
#     print("Not found : 3")

for i in range(2, 10) :
    for j in range(1, 10) :
        print(f"{i} * {j} = {i * j}")