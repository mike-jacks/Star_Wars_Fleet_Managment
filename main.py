from star_wars_ships import ShipType
from star_wars_fleet_management import FleetManager
from rebel_ships import RebelShip, XWing, YWing, AWing, BWing, CR90Corvette, MonCalamariStarCruiser, YT1300LightFreighter, UWing
from imperial_ships import ImperialShip, TIEFighter, TIEInterceptor, TIEBomber, TIEAdvanced, TIEDefender, LambdaClassShuttle, ImperialIClassStarDestroyer, ImperialIIClassStarDestroyer, ImperialSuperStarDestroyer, DeathStar, Firespray31
def main():
    # Create fleet managers
    rebel_fleet_manager = FleetManager(fleet_name="Rebel", ship_alliance=RebelShip)
    imperial_fleet_manager = FleetManager(fleet_name="Imperial", ship_alliance=ImperialShip)

    # Create rebel ships
    x_wing = XWing(name="X-Wing", ship_type=ShipType.FIGHTER, weapon_power=10, shield_power=100)
    y_wing = YWing(name="Y-Wing", ship_type=ShipType.BOMBER, weapon_power=20, shield_power=150)
    a_wing = AWing(name="A-Wing", ship_type=ShipType.INTERCEPTOR, weapon_power=15, shield_power=80)
    b_wing = BWing(name="B-Wing", ship_type=ShipType.BOMBER, weapon_power=30, shield_power=120)
    cr90_corvette = CR90Corvette(name="CR90 Corvette", ship_type=ShipType.CAPITAL, weapon_power=50, shield_power=500)
    millenium_falcon = YT1300LightFreighter(name="Millenium Falcon", ship_type=ShipType.UNIQUE, weapon_power=40, shield_power=250)
    u_wing = UWing(name="U-Wing", ship_type=ShipType.TRANSPORT, weapon_power=17, shield_power=90)
    star_cruiser = MonCalamariStarCruiser(name="Mon Calamari Star Cruiser", ship_type=ShipType.CAPITAL, weapon_power=200, shield_power=2000)

    # Create imperial ships
    tie_fighter = TIEFighter(name="TIE Fighter", ship_type=ShipType.FIGHTER, weapon_power=10, shield_power=90)
    tie_interceptor = TIEInterceptor(name="TIE Interceptor", ship_type=ShipType.INTERCEPTOR, weapon_power=15, shield_power=75)
    tie_bomber = TIEBomber(name="TIE Bomber", ship_type=ShipType.BOMBER, weapon_power=20, shield_power=140)
    tie_advanced = TIEAdvanced(name="TIE Advanced", ship_type=ShipType.FIGHTER, weapon_power=25, shield_power=160)
    tie_defender = TIEDefender(name="TIE Defender", ship_type=ShipType.INTERCEPTOR, weapon_power=30, shield_power=200)
    imperial_lambda_shuttle = LambdaClassShuttle(name="Lambda Shuttle", ship_type=ShipType.TRANSPORT, weapon_power=5, shield_power=50)
    imperial_star_destroyer_class_I = ImperialIClassStarDestroyer(name="Imperial I-Class Star Destroyer", ship_type=ShipType.CAPITAL, weapon_power=100, shield_power=1000)
    imperial_star_destroyer_class_II = ImperialIIClassStarDestroyer(name="Imperial II-Class Star Destroyer", ship_type=ShipType.CAPITAL, weapon_power=150, shield_power=1500)
    imperial_super_star_destroyer_executor = ImperialSuperStarDestroyer(name="Executor", ship_type=ShipType.CAPITAL, weapon_power=200, shield_power=2000)
    death_star = DeathStar(name="Death Star", ship_type=ShipType.UNIQUE, weapon_power=500, shield_power=10000)

    # Add ships to fleet
    rebel_fleet_manager.add_ship(x_wing)
    rebel_fleet_manager.add_ship(y_wing)
    rebel_fleet_manager.add_ship(a_wing)
    rebel_fleet_manager.add_ship(b_wing)
    rebel_fleet_manager.add_ship(cr90_corvette)
    rebel_fleet_manager.add_ship(millenium_falcon)
    rebel_fleet_manager.add_ship(u_wing)
    rebel_fleet_manager.add_ship(star_cruiser)

    imperial_fleet_manager.add_ship(tie_fighter)
    imperial_fleet_manager.add_ship(tie_interceptor)
    imperial_fleet_manager.add_ship(tie_bomber)
    imperial_fleet_manager.add_ship(tie_advanced)
    imperial_fleet_manager.add_ship(tie_defender)
    imperial_fleet_manager.add_ship(imperial_lambda_shuttle)
    imperial_fleet_manager.add_ship(imperial_star_destroyer_class_I)
    imperial_fleet_manager.add_ship(imperial_star_destroyer_class_II)
    imperial_fleet_manager.add_ship(imperial_super_star_destroyer_executor)
    imperial_fleet_manager.add_ship(death_star)

    # Print total attack power
    print("Rebel fleet:")
    print()
    rebel_fleet_manager.print_total_attack_power()
    rebel_fleet_manager.list_fleet()
    print()
    print()
    print("Imperial fleet:")
    print()
    imperial_fleet_manager.print_total_attack_power()
    imperial_fleet_manager.list_fleet()
    print()
    print()
    rebel_fleet_manager.remove_ships_out_of_commission()
    imperial_fleet_manager.remove_ships_out_of_commission()
    print()
    current_rebel_ship = rebel_fleet_manager.get_ship("X-Wing")
    current_imperial_ship = imperial_fleet_manager.get_ship("TIE Fighter")
    while current_rebel_ship.shield_power > 0 and current_imperial_ship.shield_power > 0:
        current_rebel_ship.attack(current_imperial_ship)
        current_imperial_ship.attack(current_rebel_ship)
    rebel_fleet_manager.remove_ships_out_of_commission()
    imperial_fleet_manager.remove_ships_out_of_commission()
    print()
    rebel_fleet_manager.list_fleet()
    print()
    imperial_fleet_manager.list_fleet()
    
    slave_one = Firespray31(name="Slave One", ship_type=ShipType.UNIQUE, weapon_power=40, shield_power=250)
    print(rebel_fleet_manager.is_an_ally(ship=slave_one))
    print(imperial_fleet_manager.is_an_ally(ship=slave_one))
    

if __name__ == "__main__":
    main()