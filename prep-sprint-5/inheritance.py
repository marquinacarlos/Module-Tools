# Inheritance
# Child extends Parent, adding change_last_name and get_full_name
# Parent does NOT have these methods — calling them on Parent causes errors

class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names: list[str] = []

    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

# Child has both Parent methods and its own methods
person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())       # Elizaveta Alekseeva
print(person1.get_full_name())  # Elizaveta Alekseeva
person1.change_last_name("Tyurina")
print(person1.get_name())       # Elizaveta Tyurina
print(person1.get_full_name())  # Elizaveta Tyurina (née Alekseeva)

# Parent only has its own methods — no get_full_name or change_last_name
person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())       # Elizaveta Alekseeva
# print(person2.get_full_name())    # AttributeError: 'Parent' has no attribute 'get_full_name'
# person2.change_last_name("Tyurina")  # AttributeError: 'Parent' has no attribute 'change_last_name'