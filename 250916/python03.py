# Dictionary = 사전
# 영어단어 서칭 => 뜻 표기
# 다른 객체지향 언어 => 딕셔너리 = 객체
# JSON 자료형태
# Javascript Object Notation => 자바스크립트 객체 표기법
# 다른 객체지향 언어 => 리스트 = 배열

# 딕셔너리는 => {key : value} => property

# 리스트 => []
# 튜플 => ()
# 딕셔너리 => {}

a = {"name": "Park", "age": 20}
b = {"arr": [1, 2, 3, 4]}
c = {
    "name": "David",
    "city": "Seoul",
    "age": 20,
    "grade": "A",
    "status": True
}

# list(), int(), float(), tuple()
d = dict([
    ("name", "park"),
    ("age", 20)
])
print(d["name"])
print(d["age"])
print(d.get("age1"))

# CRUD
# Create
# Read
# Update
# Delete

print(c)

c["address"] = "mapo"
print(c)