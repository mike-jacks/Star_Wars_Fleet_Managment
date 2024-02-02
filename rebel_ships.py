from star_wars_ships import StarWarsShip, ShipType

class RebelShip(StarWarsShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

class XWing(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 4

class YWing(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 8

class AWing(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 2

class BWing(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 6

class CR90Corvette(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 15

class MonCalamariStarCruiser(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 40

class YT1300LightFreighter(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 12

class UWing(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 3

class VCX100LightFreighter(RebelShip):
    def __init__(self, name: str, ship_type: ShipType, weapon_power: int) -> None:
        super().__init__(name, ship_type, weapon_power)

    def attack_power(self):
        return self.weapon_power * 1

