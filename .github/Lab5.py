# Callie Walker, Lesdy Galvez, Hanna Magen,
# Course: CS151, Dr. Rajeev
# Date: 10/21/21
# Lab Number: 5
# Program Inputs: dimensions of each room, and desired type of flooring
# Program Outputs: cost of each room, total output

def dimensions(l,w):
    return l*w
def floor(room):
    cost = 0
    user_input = input("What type of floor would you like? ")
    user_input = user_input.strip().lower()
    length = int(input("Enter length for this floor "))
    width = int(input("Enter width for this floor "))

    if (user_input == "hardwood"):
        cost = dimensions(length, width) * 1.39
        cost = round(cost, 2)
        print("Cost of floor", room, "is $", cost)
    elif (user_input == "tile"):
        cost = dimensions(length, width) * 3.99
        cost = round(cost, 2)
        print("Cost of floor", room, "is $", cost)
    elif (user_input == "carpet"):
        cost = dimensions(length, width) * 4.99
        cost = round(cost,2)
        print("Cost of floor", room, "is $", cost)
    else:
        print("invalid option, skipping room")
    return cost
def main():
    total = 0
    total += floor(1)
    total += floor(2)
    total += floor(3)
    total += floor(4)
    total += floor(5)
    total = round(total, 2)
    print("The total cost for all floors is $", total)

main()

