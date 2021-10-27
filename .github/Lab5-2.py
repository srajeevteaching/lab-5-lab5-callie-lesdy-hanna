# Callie Walker, Lesdy Galvez, Hanna Magen,
# Course: CS151, Dr. Rajeev
# Date: 10/21/21
# Lab Number: 5
# Program Inputs: dimensions of each room, and desired type of flooring
# Program Outputs: cost of each room, total output
cost = 0
total = 0
def floor(l, w):

    dimensions = l*w
    user_input = input("What type of flooring would you like? ")
    user_input = user_input.strip().lower()
    if (user_input == "hardwood"):
        cost = dimensions * 1.39
        cost = round(cost, 2)
    elif (user_input == "carpet"):
        cost += dimensions * 3.99
        cost = round(cost, 2)
    elif (user_input == "tile"):
        cost += dimensions * 4.99
        cost = round(cost, 2)
    else:
        cost = 0
        print("invalid option, skipping room, the cost is", cost)
    total += cost
    print("The cost of the room is $", cost, "The total cost is $", total)

    return dimensions

length1 = int(input("Enter length for floor 1 "))
width1 = int(input("Enter width for floor 1 "))
print("Floor 1 area is ", floor(length1, width1))

length2 = int(input("Enter length for floor 2 "))
width2 = int(input("Enter width for floor 2 "))
print("Floor 2 area is ", floor(length2, width2))

length3 = int(input("Enter length for floor 3 "))
width3 = int(input("Enter width for floor 3 "))
print("Floor 3 area is ", floor(length3, width3))

length4 = int(input("Enter length for floor 4 "))
width4 = int(input("Enter width for floor 4 "))
print("Floor 4 area is", floor(length4, width4))

length5 = int(input("Enter length for floor 5 "))
width5 = int(input("Enter width for floor 5 "))
print("Floor 5 area is ", floor(length5, width5))



