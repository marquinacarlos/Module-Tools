# Dataclasses
# Using @dataclass to auto-generate constructor, __str__, and __eq__
# Also uses date_of_birth and is_adult method

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age >= 18

imran = Person("Imran", date(2003, 5, 15), "Ubuntu")
imran2 = Person("Imran", date(2003, 5, 15), "Ubuntu")
eliza = Person("Eliza", date(1991, 8, 20), "Arch Linux")

print(imran)                # Person(name='Imran', date_of_birth=..., ...)
print(imran == imran2)      # True — dataclass compares fields
print(imran == eliza)       # False
print(imran.is_adult())     # True