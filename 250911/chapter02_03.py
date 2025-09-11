# 문자열

str1 = "Hello Python!"
str2 = 'Hello Python!'
str3 = """Hello Python!"""
str4 = '''Hello Python!'''

print(type(str1), type(str2), type(str3), type(str4))

# 문자열의 길이를 확인하고자 할 때
print(len(str1))

print('I\'m\' a" Boy') # escape sequence
print("a\tb") # escape sequence
print("a\nb") # escape sequence

raw_s1 = r"C:\Users\Admin\Documents\python_class\250911"

print(raw_s1)

# 멀티라인
multi_str = \
'''
String
Multi Line
Test
'''

print(multi_str)

str_01 = "python"
str_02 = "Apple"

print(str_01 * 3)

# in 구문 : in => 어딘가 안에 있다 의미!!
# not in 구문 : not in => 어딘가 안에 없다 의미!!


print("a" in str_01) # 회원가입
print("y" not in str_02)

str_03 = "Good Morning"
str_04 = "02-123-5678"

print("Capitalize : ", str_01.capitalize())
print("Endswith? : ", str_01.endswith("y"))
print("replace? : ", str_01.replace("thon", "Good"))
print("sorted? : ", sorted(str_01))
print("split? : ", str_04.split("-")[0])

