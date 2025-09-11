# 숫자 맞추기 게임

secret = 7

guess = int(input("1부터 10사이의 숫자를 입력하세요 : "))

if guess == secret :
    print("정답😊!")
elif guess < secret :
    print("너무 작아요🤣!")
else :
    print("너무 커요😁!")