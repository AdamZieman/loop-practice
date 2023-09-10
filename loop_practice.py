# loop_practice.py
# Demonstrates the programmers understanding of iteration with 4 examples:
#   A) Iterate using range() and a hardcoded value
#   B) Iterate through a list
#   C) Iterate using range() and an inputted value
#   D) Iterate using range() to calculate a summation

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 3

# Author: Adam Zieman
# Date: March 9, 2021

def main():
    # Prints a heading for the program
    print("Adam Zieman - Loop Practice Spring 2021")
    print("-------------------------------------")
    
    # SECTION A
    # Prints a heading and description of the section
    print("----- Section A -----")
    print("Printing a season name (4 times)")
    print("-----------------------------------------")

    # Print a statement 4 times
    for i in range(4):
        print("My favorite season of the year is Summer")

    print()
   
    # SECTION B
    # Prints a heading and description of the section
    print("----- Section B -----")
    print("Demostrate Printing Numbers Based on a List")
    print("-------------------------------------------")

    # Iterate through a list and print the three less than the indexed value
    for n in [5, 9, 14, 7, 6]:
        print("Original number from list:", n)
        print(n ,"minus 3 equals", n - 3)

    print()

    # SECTION C
    # Prints a heading
    print("----- Section C -----")
    sport = eval(input("Enter times to print a name of a sport: ")) # User inputs the quantity to print
    print("Printing a sport", sport, "times") # Section description
    print("--------------------------------")

    # Loop the amount of times specified by the user
    for s in range(sport):
        s = s + 1 # Increment the counter
        # Print the iteration count and the message to be printed
        print("(",s,")", sep='', end=' ')
        print("Sport: Modern pentathlon")

    print()

    # SECTION D
    # Prints a heading and description for the section
    print("----- Section D -----")
    print("Starting from 0, will add", sport - 1, "numbers.")
    print("Each number will be multiplied by 25 before adding.")
    
    result = 0

    # Loop is executed one less time than the number entered in section C
    for r in range(sport - 1):
        # User inputs a single-digit number
        num = eval(input("Enter a single-digit number: "))

        num = num * 25 # Increments num by the product of itself by 25
        result = result + num # Increments result by num
        
        # Prints the value which was added to result
        print("Value to add:", num)

    # prints number of times ran and sum of result
    print("Result after adding", sport - 1, "numbers =", result)
    
main() # Calls the main() function
