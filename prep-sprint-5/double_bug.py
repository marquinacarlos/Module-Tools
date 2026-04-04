# Limits of type checking
# The bug: function is called "double" but multiplies by 3
# Type checking can't catch this — the types are correct, the logic is wrong

def double(number: int) -> int:
    return number * 2  # Fixed: was * 3

print(double(10))  # 20