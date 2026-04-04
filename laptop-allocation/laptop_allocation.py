from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: List[OperatingSystem]

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def sadness(person: Person, laptop: Laptop) -> int:
    """Calculate how sad a person is with a given laptop."""
    try:
        return person.preferred_operating_system.index(laptop.operating_system)
    except ValueError:
        return 100


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    """Allocate laptops to people minimizing total sadness."""
    allocation: Dict[Person, Laptop] = {}
    available = list(laptops)

    # Sort people by how few preferences they have (most constrained first)
    sorted_people = sorted(people, key=lambda p: len(p.preferred_operating_system))

    for person in sorted_people:
        best_laptop = None
        best_sadness = 101

        for laptop in available:
            s = sadness(person, laptop)
            if s < best_sadness:
                best_sadness = s
                best_laptop = laptop

        if best_laptop is not None:
            allocation[person] = best_laptop
            available.remove(best_laptop)

    return allocation


# Test
people = [
    Person(name="Imran", age=22, preferred_operating_system=[OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
    Person(name="Eliza", age=34, preferred_operating_system=[OperatingSystem.ARCH]),
    Person(name="Kai", age=28, preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

result = allocate_laptops(people, laptops)

total_sadness = 0
for person, laptop in result.items():
    s = sadness(person, laptop)
    total_sadness += s
    print(f"{person.name} -> {laptop.manufacturer} {laptop.model} ({laptop.operating_system.value}) | sadness: {s}")

print(f"\nTotal sadness: {total_sadness}")