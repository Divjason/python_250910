# def first_func(w) :
#     print(f"Hello {w}")

# def first_func(w) :
#     value = "Hello " + w
#     return value

# word = "World"

# func_word = first_func(word)

# print(func_word)

# 다중 반환

# def func_mul(x) :
#     y1 = x * 10
#     y2 = x * 20
#     y3 = x * 30
#     return y1, y2, y3

# tup = func_mul(10)
# list_tup = list(tup)

# for item in list_tup :
#     print(item)

# def args_func(x = 10) :
#     print(x)

# def args_func(**args) :
#     for i ,v in enumerate(args) :
#         print(f"{i + 1}. {v}")

def args_func(**args) :
    for v in args.keys() :
        print(v, args[v])


args_func(name1 = "David", name2 = "Romeo", name3 = "Peter")
# args_func({"name": "David"})