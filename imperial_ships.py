from star_wars_ships import StarWarsShip, ShipType

class ImperialShip(StarWarsShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)

class TIEFighter(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)

    def attack_power(self):
        return self.weapon_power * 2

class TIEInterceptor(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)
    
    def attack_power(self):
        return self.weapon_power * 3

class TIEBomber(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)

    def attack_power(self):
        return self.weapon_power * 8

class TIEAdvanced(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)
   
    def attack_power(self):
        return self.weapon_power * 4

class TIEDefender(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)
   
    def attack_power(self):
        return self.weapon_power * 5

class LambdaClassShuttle(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)


    def attack_power(self):
        return self.weapon_power * 1

class ImperialIClassStarDestroyer(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)

    def attack_power(self):
        return self.weapon_power * 25

class ImperialIIClassStarDestroyer(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)

    def attack_power(self):
        return self.weapon_power * 30

class ImperialSuperStarDestroyer(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)

    def attack_power(self):
        return self.weapon_power * 50

class DeathStar(ImperialShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int, shield_power:int) -> None:
        super().__init__(name, ship_type, weapon_power, shield_power)

    def attack_power(self):
        return self.weapon_power * 1000

