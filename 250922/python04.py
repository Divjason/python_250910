import random

words = ["python", "banana", "zodiac", "fortune", "hangman"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("🤞 단어 추측게임(hangman) 시작")
print("😜 단어를 맞춰보세요! 총 기회는 6회 입니다.")

while attempts > 0 :
    guess = input("글자 하나를 입력하세요!").lower()

    if guess in word :
        print("문자 1개를 맞추셨습니다!")
    else :
        attempts -= 1
        print("틀렸습니다.남은기회 : ", attempts)