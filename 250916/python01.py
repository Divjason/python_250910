import copy # module | library

c = [70, 75, 80, 85]

print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# 복사 = copy
# 변수 => 원시타입 // 참조타입
# stack // heap => call stack

temp = c
print(temp, c)

# temp => [70, 75, 80, 85]
# c => [70, 75, 80, 85]

# 파이썬 시퀀스 형태의 자료구조 => 참조타입
# (주소)참조

print(id(c))
print(id(temp))


d = [[1, 2], [3, 4]]

shallow = copy.copy(d)

print(f"얕은복사 : {shallow}")
print(f"id 비교 : {id(d)}, {id(shallow)}")
print(f"내부 값 비교 : {id(d[0])}, {id(shallow[0])}")

# 얕은 복사 : a변수 => b변수 복제

deep = copy.deepcopy(d)

print(f"원본 : {d}")
print(f"깊은복사 : {deep}")
print(f"id 비교 : {id(d)}, {id(deep)}")
print(f"내부 값 비교 : {id(d[0])}, {id(deep[0])}")

d[0][0] = 999

print(f"원본 : {d}")
print(f"얕은복사 : {shallow}")
print(f"깊은복사 : {deep}")

# 파이썬 > 사용자에 어떤 값을 받아서 변수할당 > 정렬, 요청
# 원본데이터 정렬요청 > 언제라도 가변적으로 바뀔 수 있음

e = [1, 2, 3, 4, 20]

del e[2] # 선언 및 할당된 리스트에서 특정 번째 인덱스 값을 제거
print(e)

e.append(5) # 리스트의 값을 순차적으로 추가
print(e)

f = [5, 2, 1, 4, 3]
f.sort() # 오름차순 정렬
print(f)

f.reverse() # 내림차순 정렬
print(f)

print(f[3]) # 대괄호 표기법 > 인덱스 적용
print(f.index(3)) # 메서드 함수를 통해서 특정번째 인덱스 값

print(f[3] == f.index(3))

f.remove(4) # 인덱스가 아닌 실제 매칭되어지는 값을 찾아서 제거
print(f)

print(f.pop()) # 특정 리스트 자료구조에서 맨 뒤에있는 값을 찾아오는 역할 (*잘라내기)
print(f)

f.append(5)
print(f)

print(f.count(5))
print(f.count(3))
print(f.count(1)) # 리스트 자료구조 안에 특정 값이 몇번 카운트가 되었는지 확인

print(f)

ex = [8, 9]

f.extend(ex)
print(f)