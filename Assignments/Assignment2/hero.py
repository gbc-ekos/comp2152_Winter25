from Assignments.Assignment2.character import Character
from Assignments.Assignment2.dice import small_roll


class Hero(Character):

    def __init__(self):
        Character.__init__(self)
        self.__roll_cs()
        self.__roll_hp()

    def __roll_cs(self):
        # Initializing hero combat strength
        while True:
            print("    ------------------------------------------------------------------")
            print("    |", end="    ")
            combat_strength = input("Enter your combat Strength (1-6): ")
            if not combat_strength.isnumeric():
                # If one of the inputs are invalid, print error message and halt
                print(
                    "    |    Invalid input. Player needs to enter integer numbers for Combat Strength    |")
                continue
            # Note: Now safe to cast combat_strength to integer
            # Validate input: Check if the string inputted
            elif int(combat_strength) not in range(1, 7):
                print("    |    Enter a valid integer between 1 and 6 only")
                continue
            else:
                break
        combat_strength = int(combat_strength)

        # Define the Weapons
        weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

        # Roll for weapon
        print("    |", end="    ")
        input("Roll the dice for your weapon (Press enter)")
        ascii_image5 = """
                              , %               .           
                   *      @./  #         @  &.(         
                  @        /@   (      ,    @       # @ 
                  @        ..@#% @     @&*#@(         % 
                   &   (  @    (   / /   *    @  .   /  
                     @ % #         /   .       @ ( @    
                                 %   .@*                
                               #         .              
                             /     # @   *              
                                 ,     %                
                            @&@           @&@
                            """
        print(ascii_image5)
        weapon_roll = small_roll()

        # Limit the combat strength to 6
        combat_strength = min(6, (combat_strength + weapon_roll))
        print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

        self.combat_strength = combat_strength

        # Weapon Roll Analysis
        print("    ------------------------------------------------------------------")
        print("    |", end="    ")
        input("Analyze the Weapon roll (Press enter)")
        print("    |", end="    ")
        if weapon_roll <= 2:
            print("--- You rolled a weak weapon, friend")
        elif weapon_roll <= 4:
            print("--- Your weapon is meh")
        else:
            print("--- Nice weapon, friend!")

        # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
        if weapons[weapon_roll - 1] != "Fist":
            print("    |    --- Thank goodness you didn't roll the Fist...")
        return

    def __roll_hp(self):
        print("    |", end="    ")
        input("Roll the dice for your health points (Press enter)")
        self.health_points = small_roll()
        print("    |    Player rolled " + str(self.health_points) + " health points")

    # Hero's Attack Function
    def hero_attacks(self, target_hp):
        ascii_image = """
                                    @@   @@ 
                                    @    @  
                                    @   @   
                   @@@@@@          @@  @    
                @@       @@        @ @@     
               @%         @     @@@ @       
                @        @@     @@@@@     
                   @@@@@        @@       
                   @    @@@@                
              @@@ @@                        
           @@     @                         
       @@*       @                          
       @        @@                          
               @@                                                    
             @   @@@@@@@                    
            @            @                  
          @              @                  

      """
        print(ascii_image)
        print("    |    Player's weapon (" + str(self.combat_strength) + ") ---> Monster (" + str(target_hp) + ")")
        if self.combat_strength >= target_hp:
            # Player was strong enough to kill monster in one blow
            target_hp = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            target_hp -= self.combat_strength

            print("    |    You have reduced the monster's health to: " + str(target_hp))
        return target_hp

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")