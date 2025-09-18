import random

print("숫자 맞추기 게임")
print("1부터 100사이의 숫자를 맞춰보세요!")

secret_number = random.randint(1, 100)
print(secret_number)

guess = int(input("당신의 추측 : "))

if guess < secret_number :
    print("너무 작아요!")
elif guess > secret_number :
    print("너무 커요!")
else :
    print("정답입니다!")
