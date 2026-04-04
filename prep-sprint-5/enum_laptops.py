# Enums
# Uses OperatingSystem enum to prevent typos and case issues
# Accepts user input, validates it, and recommends laptops

import sys
from dataclasses import dataclass
from enum import Enum
from typing import List

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

name = input("Enter your name: ")

age_str = input("Enter your age: ")
try:
    age = int(age_str)
except ValueError:
    print(f"Invalid age: {age_str}", file=sys.stderr)
    sys.exit(1)

os_str = input(f"Enter preferred OS ({', '.join(os.value for os in OperatingSystem)}): ")
try:
    preferred_os = OperatingSystem(os_str)
except ValueError:
    print(f"Invalid operating system: {os_str}", file=sys.stderr)
    sys.exit(1)

person = Person(name=name, age=age, preferred_operating_system=preferred_os)

matching = [l for l in laptops if l.operating_system == person.preferred_operating_system]
print(f"We have {len(matching)} laptop(s) with {preferred_os.value}.")

os_counts: dict[OperatingSystem, int] = {}
for laptop in laptops:
    os_counts[laptop.operating_system] = os_counts.get(laptop.operating_system, 0) + 1

most_available_os = max(os_counts, key=lambda k: os_counts[k])
if most_available_os != preferred_os and os_counts[most_available_os] > len(matching):
    print(f"Tip: if you're willing to use {most_available_os.value}, we have {os_counts[most_available_os]} laptop(s) available.")