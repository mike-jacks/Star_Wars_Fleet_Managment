from star_wars_ships import StarWarsShip, ShipType

class FleetManager:
    def __init__(self) -> None:
        self.fleet: dict[ShipType,list[StarWarsShip]] = dict()    
    
    def add_ship(self, ship: StarWarsShip):
        if ship.ship_type in self.fleet:
            self.fleet[ship.ship_type].append(ship)
        else:
            self.fleet[ship.ship_type] = [ship]
    
    def remove_ship(self, ship: StarWarsShip):
        if ship.ship_type in self.fleet:
            self.fleet[ship.ship_type].remove(ship)
        else:
            print(f"{ship.name} not found in the fleet")
    
    def calculate_total_attack_power(self):
        total_attack_power = 0
        for ships in self.fleet.values():
            for ship in ships:
                total_attack_power += ship.attack_power()
        return total_attack_power

    def print_total_attack_power(self):
        print(f"Total attack power: {self.calculate_total_attack_power()}")