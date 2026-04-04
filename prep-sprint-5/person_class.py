# Classes and objects
# mypy catches that Person has no 'address' property
# Also demonstrates is_adult as a free function
# And a function that accesses a non-existent property to trigger mypy error

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

def is_adult(person: Person) -> bool:
    return person.age >= 18

# This function intentionally triggers a mypy error
# def get_address(person: Person) -> str:
#     return person.address  # error: "Person" has no attribute "address"

imran = Person("Imran", 22, "Ubuntu")
eliza = Person("Eliza", 34, "Arch Linux")

print(imran.name)       # Imran
print(eliza.name)       # Eliza
print(is_adult(imran))  # True
print(is_adult(eliza))  # True

# These would cause mypy errors:
# print(imran.address)
# print(eliza.address)