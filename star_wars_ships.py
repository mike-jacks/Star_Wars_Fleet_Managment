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
        target.shield_power -= self.attack_power()