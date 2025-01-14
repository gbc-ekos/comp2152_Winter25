import random

combatStrength = 0
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear bomb']
weaponRoll = random.randint(1, 6)
combatStrength+= weaponRoll

try:
    print("Hero weapon: " + weapons[combatStrength-1])
except IndexError:
    print("Index out of bounds for weapons")
    exit(1)

if weaponRoll <= 2:
    print("You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("Your weapon is meh")
else:
    print("Nice weapon, friend!")
if weaponRoll > 1:
    print("Thank goodness you didn't roll the Fist...")