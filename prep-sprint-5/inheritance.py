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

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())       # Elizaveta Alekseeva
print(person1.get_full_name())  # Elizaveta Alekseeva
person1.change_last_name("Tyurina")
print(person1.get_name())       # Elizaveta Tyurina
print(person1.get_full_name())  # Elizaveta Tyurina (née Alekseeva)

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())       # Elizaveta Alekseeva
# print(person2.get_full_name())  # ERROR: Parent doesn't have get_full_name
# person2.change_last_name("Tyurina")  # ERROR: Parent doesn't have change_last_name