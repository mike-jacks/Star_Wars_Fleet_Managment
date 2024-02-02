from abc import ABC, abstractmethod
from enum import Enum

class ShipType(Enum):
    FIGHTER = "Fighter"
    INTERCEPTOR = "Interceptor"
    BOMBER = "Bomber" 
    SUPPORT = "Support"
    TRANSPORT = "Transport"
    CAPITAL = "Capital"
    UNIQUE = "Unique"

class StarWarsShip(ABC):
    def __init__(self, name: str, ship_type:ShipType, weapon_power: int, shield_power: int) -> None:
        self.name = name
        self.ship_type = ship_type
        self.weapon_power = weapon_power
        self.shield_power = shield_power
    
    @abstractmethod
    def attack_power(self):
        pass
    
    def attack(self, target: 'StarWarsShip'):
        if self.shield_power > 0:
            print(f"{self.name} is attacking {target.name}")
            print(f"{self.name} attack power: {self.attack_power()}")
            print(f"{target.name} shield power: {target.shield_power}")
            print(f"{target.name} shield power after attack: {target.shield_power - self.attack_power()}")
            target.shield_power -= self.attack_power()
            if target.shield_power < 0:
                target.shield_power = 0
        else:
            print(f"{self.name} is out of commission and cannot attack")