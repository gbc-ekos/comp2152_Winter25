from Assignments.Assignment2.character import Character
from Assignments.Assignment2.dice import big_roll


class Monster(Character):
    def __init__(self):
        Character.__init__(self)
        self.__roll_cs()
        self.__roll_hp()

    def __roll_cs(self):
        while True:
            print("    ------------------------------------------------------------------")
            print("    |", end="    ")
            m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

            # Validate input: Check if the string inputted is numeric
            if not m_combat_strength.isnumeric():
                # If one of the inputs are invalid, print error message and halt
                print("    |    Invalid input. Player needs to enter integer numbers for Combat Strength    |")
                continue

            # Note: Now safe to cast combat_strength to integer
            # Validate input: Check if the string inputted
            elif int(m_combat_strength) not in range(1, 7):
                print("    |    Enter a valid integer between 1 and 6 only")
                continue
            else:
                break

        self.combat_strength = int(m_combat_strength)

    def __roll_hp(self):
        # Roll for monster health points
        print("    |", end="    ")
        input("Roll the dice for the monster's health points (Press enter)")
        m_health_points = big_roll()
        print("    |    Player rolled " + str(m_health_points) + " health points for the monster")
        self.health_points = int(m_health_points)

    # Monster's Attack Function
    def monster_attacks(self, target_hp):
        ascii_image2 = """                                                                 
               @@@@ @                           
          (     @*&@  ,                         
        @               %                       
         &#(@(@%@@@@@*   /                      
          @@@@@.                                
                   @       /                    
                    %         @                 
                ,(@(*/           %              
                   @ (  .@#                 @   
                              @           .@@. @
                       @         ,              
                          @       @ .@          
                                 @              
                              *(*  *      
                 """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(self.combat_strength) + ") ---> Player (" + str(target_hp) + ")")
        if self.combat_strength >= target_hp:
            # Monster was strong enough to kill player in one blow
            target_hp = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            target_hp -= self.combat_strength
            print("    |    The monster has reduced Player's health to: " + str(target_hp))
        return target_hp

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
