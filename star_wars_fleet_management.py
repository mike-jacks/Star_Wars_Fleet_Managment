from star_wars_ships import StarWarsShip, ShipType

class FleetManager:
    def __init__(self, fleet_name) -> None:
        self.fleet_name = fleet_name
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

    def list_fleet(self):
        print(f"{self.fleet_name} fleet:")
        for ship_type, ships in self.fleet.items():
            print(f"{ship_type.value} ships:")
            for ship in ships:
                print(f"  - {ship.name}")
    
    def calculate_total_shield_power(self):
        total_defense_power = 0
        for ships in self.fleet.values():
            for ship in ships:
                total_defense_power += ship.defense_power()
        return total_defense_power
    
    def print_total_shield_power(self):
        print(f"Total shield power: {self.calculate_total_shield_power()}")
    
    def remove_ships_out_of_commission(self):
        for ships in self.fleet.values():
            for ship in ships:
                if ship.shield_power == 0:
                    self.remove_ship(ship)
                    print(f"{ship.name} has been destroyed and removed from the fleet")
                    
    def get_ship(self, ship_name: str) -> StarWarsShip | None:
        for ships in self.fleet.values():
            for ship in ships:
                if ship.name == ship_name:
                    return ship
        return None
    
    def ship_attack(self, attacker: StarWarsShip, target: StarWarsShip):
        if attacker.shield_power > 0:
            attacker.attack(target)
        else:
            print(f"{attacker.name} is out of commission and cannot attack")