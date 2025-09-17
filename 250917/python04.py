# BMI

height = float(input("키를 입력하세요(cm) : ")) / 100
weight = float(input("몸무게를 입력하세요(kg) : "))

bmi = weight / (height ** 2)
print(f"당신의 BMI : {round(bmi, 2)}")

if bmi < 18.5 :
    print("저체중 😒")
elif 18.5 <= bmi < 23 :
    print("정상 😁")
elif 23 <= bmi < 25 :
    print("과체중 😢")
else :
    print("비만 🤢")