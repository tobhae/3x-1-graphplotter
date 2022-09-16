# A simple program for plotting 3x+1
# https://github.com/tobhae/3x-1-graphplotter

from matplotlib import pyplot as plt

result_list = []
int_check = False

# Test user input for integer
while int_check != True:
    try:
        num = int(input("Enter a integer: "))
        int_check = True
    except ValueError:
        print("Not valid, enter a integer as input.")
    
# The first number is appended to the list so the graph tells us were we started
result_list.append(num)

# Function for calculating 3x+1
def calculate(num):
  
    # Base case
    if num == 1:
        return

    # Calculate even or uneven numbers
    elif num % 2 == 0:
        new_num = int(num / 2)

    else:
        new_num = int(num * 3 + 1)
    
    # Append calculated number to list and use a recursive function call
    result_list.append(new_num)
    calculate(new_num)
    return

# Run the function with user input
calculate(num)

# Plot graph using list with calculated numbers
plt.plot(result_list)
plt.xlabel("Iterations")
plt.ylabel("Number")
# plt.savefig saves the graph as a .PNG file
plt.savefig(f"3x+1Number{num}")
plt.show()