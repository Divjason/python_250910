import random

print("😍지금부터 운명의 가위.바위.보 게임을 시작합니다!🤞")

choices = ["가위", "바위", "보"]

user = input("가위.바위.보 중 하나를 입력하세요! : ")
computer = random.choice(choices)

print(f"당신의 선택 : {user} VS 컴퓨터의 선택 : {computer}")

if user == computer :
    print("비겼습니다.")
elif (user == "가위" and computer == "보") or (user == "바위" and computer == "가위") or (user == "보" and computer == "바위") :
    print("이겼습니다.")
else :
    print("졌습니다.")