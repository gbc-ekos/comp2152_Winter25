# Sample Coding Questions 01 Week 01
# Eduard Kosenko, 101480050

#Defining variables
mArray = [1,4,7,9]

#Order of operations
a = 1
b = 2
c = 3
d = 4
e = a - ((b ** c) // d) + (a % c)

#Formatting
temperature = 32.6
print("The temperature today is: {temp:.3f} degrees Celsius".format(temp=temperature))

#Common Functions
print("Enter your age: ", end='')
userAge = int(input())
print(f"Now showing the shop items filtered by age: {userAge}")

