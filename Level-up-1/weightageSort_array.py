# Import the math module to use mathematical functions.
import math

# Define a function to calculate the weight of a number.
def weight_calc(num):
    weight = 0
    
    # Check if the number is a perfect square.
    if (is_perfect_square(num)):
        weight += 5
    
    # Check if the number is divisible by 4 and 6.
    if (num % 4 == 0) and (num % 6 == 0):
        weight += 4
    
    # Check if the number is even.
    if (num % 2 == 0):
        weight += 3
    
    return weight

# Define a function to check if a number is a perfect square.
def is_perfect_square(num):
    square = int(math.sqrt(num))
    return (square * square == num)

# Input: Read the number of elements.
n = int(input())

# Input: Read a list of numbers from the user.
nums = [int(x) for x in input().split()]

# Create an empty dictionary to store numbers as keys and their weights as values.
my_dict = {}

# Calculate the weight for each number and store it in the dictionary.
for num in nums:
    my_dict[num] = weight_calc(num)

# Sort the numbers based on their weights in ascending order.
sorted_nums = sorted(my_dict.keys(), key=lambda x: (my_dict[x], x))

# Output: Print the sorted numbers separated by spaces.
print(*sorted_nums, sep=' ')
