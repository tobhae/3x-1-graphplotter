# A simple program for plotting 3x+1

# Rules for 3x+1:
# If number is even, divide by 2.
# If number is uneven, multiply by 3 and add 1.
# When number reaches 1 it will be stuck in a infinite loop going 
# back and forth between 4, 2 and 1, here the program will end.

from matplotlib import pyplot as plt

result_list = []

# User inputs which number should be calculated
num = int(input("Enter a number: "))

# The first number is appended to the list so the graph tells us were we started
result_list.append(num)

# Function for calculating 3x+1
def calculate(num):
    
    # Base case
    if num == 1:
        return
    
    # If number is even, divide by 2 and append new number to list
    # Use a recursive function call with the new number
    elif num % 2 == 0:
        new_num = int(num / 2)
        result_list.append(new_num)
        calculate(new_num)

    # If uneven, multiply by 3 and add 1. Append new number to list
    # Use a recursive function call with the new number
    else:
        new_num = int(num * 3 + 1)
        result_list.append(new_num)
        calculate(new_num)

# Run the function with user input
calculate(num)

# Plot graph using our list with calculated numbers
plt.plot(result_list)
plt.show()