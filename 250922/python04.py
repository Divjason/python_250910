import random

def hangman() :
    words = ["python", "banana", "zodiac", "fortune", "hangman"]
    word = random.choice(words)
    print(word)
    guessed = ["_"] * len(word)
    attempts = 10

    print("🤞 단어 추측게임(hangman) 시작")
    print("😜 단어를 맞춰보세요! 총 기회는 6회 입니다.")

    while attempts > 0 :
        print("현재상태 : ", " ".join(guessed)) # p y t h o n
        guess = input("글자 하나를 입력하세요!").lower()

        if guess in word :
            for index, char in enumerate(word) :
                if guess == char :
                    guessed[index] = guess
                    print("문자 1개를 맞추셨습니다!")
            if "_" not in guessed :
                print("정답입니다! 단어 : ", word)
                break
        else :
            attempts -= 1
            print("틀렸습니다.남은기회 : ", attempts)

    if "_" in guessed :
        print(f"실패! 정답은 {word} 입니다!")

hangman()
# 개발자 연봉 => 생성형 AI
# 코드들을 정말 다양하고 복잡한 구조로 연결해서 사회적인 문제를 해결할 수 있는 제품 선보이는 게
# 요즘 신입 주니어 개발자들의 코딩 실력 x
# 생성형 AI => 문제, 문제해결 범위 10개 => 100개
