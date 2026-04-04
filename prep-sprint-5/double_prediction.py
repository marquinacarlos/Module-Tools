# Why we use types - exploring type behavior

def half(value):
    return value / 2

def double(value):
    return value * 2

def second(value):
    return value[1]

# half examples
print(half(22))        # 11.0
# print(half("hello")) # TypeError: unsupported operand type(s)
# print(half("22"))    # TypeError: unsupported operand type(s)

# double examples
print(double(22))       # 44
print(double("hello"))  # "hellohello" — repeats the string
print(double("22"))     # "2222" — repeats "22" twice, does NOT return 44

# second examples
# print(second(22))    # TypeError: 'int' object is not subscriptable
# print(second(0x16))  # TypeError: same thing, 0x16 is just 22 as int
print(second("hello"))  # "e" — second character
print(second("22"))     # "2" — second character