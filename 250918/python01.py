# 조건문 : 조건식 참이면 실행!
# 논리연산자 : and / or / not
# and : a and b : a도 참이고, b도 참이어야 최종 참
# or : a or b : a가 참이거나, b가 참이면 최종 참
# not : not 연산식 => 해당 연산식이 부정이면 참

# a = 75
# b = 40
# c = 10

# print(a > b and b > c)
# print(a > b and b < c)
# print(a > b or b < c)
# print(a < b or b < c)
# print(not b < c)
# print(not b > c)

# score1 = 70
# score2 = "A"

# if score1 >= 90 or score2 == "A" :
#     print("Pass")
# else :
#     print("Fail")

# id1 = "vip" # "=" -> 할당 VS "==" -> 좌항과 우항이 같다
# id2 = "admin"
# grade = "platinum"

# if id1 == "vip" or id2 == "admin" :
#     print("관리자 입장!")

# if id2 == "admin" and grade == "platinum" :
#     print("최상위 관리자")

# elif => elif -> if 조건문 & else문 만 가지고 양자택일 할 수 없는 경우를 대비
# 사용하고자하는 갯수 제약 조건 x
# elif는 반드시 else 보다 먼저 사용!

num = 70

if num >= 90 :
    print("Grade : A")
elif num >= 80 :
    print("Grade : B")
elif num >= 70 :
    print("Grade : C")
else :
    print("과락")