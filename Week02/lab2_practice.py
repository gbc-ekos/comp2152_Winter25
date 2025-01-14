import random

elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon']
print("Elements: ", elements)

# def func():
#     return True
# def say_greeting(name, message="Hi"):
#     print(f"{message}, {name}")
#
# say_greeting("Jim")
# say_greeting("Jim", "Hello")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer")
            continue

try:
    elementSelected = get_valid_int_input("Enter the index of the element you like: ")
    # Roll dice
    elementRoll = random.randint(1, 6)
    totalNum = elementSelected + elementRoll

    #Print the result based on the totalNum
    if elementRoll <= 2:
        print("You rolled a weak element, friend.")
    elif elementRoll <= 4:
        print("Your element is moderate.")
    else:
        print("Nice element.")
except IndexError:
    print("Invalid element index!")
except Exception as e:
    print("Unexpected error: ", e)