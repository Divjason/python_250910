class Dog :
    # 클래스 선언 시, 아래처럼 속성을 선언
    species = "firstdog"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Dog (name={self.name}, age={self.age})"
    
print(Dog)

a = Dog("micky", 2)
b = Dog("baby", 3)

# 비록 부모는 1개 => 복제품 인스턴스 객체는 서로 다른 주소값

print(a)
print(b)

print(a == b, id(a), id(b))

# print(dir(a))
print(f"a : {a.__dict__}")
print(f"b : {b.__dict__}")

print(a)

print("{} is a {}".format(a.name, a.age))

print(a.species)