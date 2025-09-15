# 자료형 > 숫자형 // 문자열
# 문자열 => 슬라이싱(slice = 나누다. 자르다) 기능
# 문자열 => sequence 자료형 중 하나
# sequence > 문자열 | 리스트 | 튜플
# sequence 범주 안에 있는 자료형들은 하나같이 동일한 특징
# 순환 => "순차적으로 변환" 할 수 있는 기능
# 해당 자료형 안에 포함되어있는 각각의 값들에게 순번을 매겨놓을 수 있어야함!
# 순번 x => index => 문자열과 같은 시퀀스형 자료구조는 해당 문자마다 각각의
# index값을 가지고 있으며, 해당 인덱스 값을 통해서 반복 순환할 수 있는 기능을 가지고 있음
# 이진수 작동 => 이진법 => 0, 1

str_sl = "Nice Python"

print(str_sl[0:4])
print(str_sl[:4]) # 해당 문자열의 시작하고자하는 첫번째 인덱스는 생략가능
print(str_sl[5:]) # 슬라이싱 마지막번째 생략 => 끝까지 찾아라!
print(len(str_sl)) # 11

print(str_sl[:len(str_sl)])

print(str_sl[1:10:2]) # 슬라이싱 기능 => 세번째 => 건너뛰기!

print(str_sl[-5:])
print(str_sl[1:9])
print(str_sl[1:-2])
print(str_sl[::2])

# 컴퓨터는 결국 거의 대부분의 자료를 숫자로 인식!!
# 문자 => 숫자 => 아스키 코드라는 시스템 처리개념이 존재!!

print(ord("a"))
print(chr(97))

# encoding // decoding