# Q1: Write a Python program that prompts the user to enter five separate integers. Use a for loop to compute the square of each integer and print each original integer along with its square immediately after it is entered.

# Sample output:

# Enter an integer: 4
# The square of 4 is 16
# Enter an integer: 4
# The square of 4 is 16
# Enter an integer: 2
# The square of 2 is 4
# Enter an integer: 7
# The square of 7 is 49
# Enter an integer: 2
# The square of 2 is 4






# for i in range(5):
#     num = int(input("Enter an integer: "))
#     square = num**2
#     print(f"The square of {num} is {square}")
    



# Q2 Write a Python program that:

# Asks the user for their working hours (a whole number).
# Asks the user to enter their ratings for three tasks (each rating is out of 100).
# The rules for getting a bonus are:

# The worker needs to have worked at least 40 hours.
# The average rating for the three tasks must be at least 60.
# If both conditions are met, print "Bonus Granted". Otherwise, print "Bonus Denied".

# Asking for working hours
working_hours = int(input("Enter working hours: "))

# Asking for ratings for three tasks
rating1 = int(input("Enter rating for Task 1: "))
rating2 = int(input("Enter rating for Task 2: "))
rating3 = int(input("Enter rating for Task 3: "))

# Calculating average rating
average_rating = (rating1 + rating2 + rating3) / 3

# Checking the bonus eligibility
if working_hours >= 40 and average_rating >= 60:
    print("Bonus Granted")
else:
    print("Bonus Denied")



# Q3: Write a Python program that:

# Asks the user for the total number of cupcakes they want to bake.
# Asks the user for the number of eggs available. Use a loop to check if they have enough eggs. Each cupcake requires 1 egg.
# The criteria for baking are as follows:
# The user must have at least 12 cupcakes to bake and at least as many eggs as cupcakes to successfully bake them.
# If both conditions are met, the program should print "Baking is successful!"
# If either condition fails, the program should print "Baking is unsuccessful."

# Asking for total number of cupcakes
total_cupcakes = int(input("Enter total number of cupcakes: "))

# Asking for number of eggs available
eggs_available = int(input("Enter the number of eggs available: "))

# Checking criteria for baking
if total_cupcakes >= 12 and eggs_available >= total_cupcakes:
    print("Baking is successful!")
else:
    print("Baking is unsuccessful.")


# Q4: Write a Python program that asks the user for two integers. If both numbers are even, multiply them, otherwise, add them. Use nested if statements and logical operators to check the number conditions

# Asking for two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Checking conditions
if num1 % 2 == 0:
    if num2 % 2 == 0:
        result = num1 * num2  # Multiplying if both are even
    else:
        result = num1 + num2  # Adding otherwise
else:
    result = num1 + num2      # Adding otherwise

print(result)


# Q5: Write a program that asks the user for the number of terms in the Fibonacci sequence they want to generate. Use a for loop to compute and print the sequence up to that number of terms.

# Asking for the number of terms
terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Initializing the first two terms
a, b = 0, 1

# Generating the Fibonacci sequence
for _ in range(terms):
    print(a, end=" ")  # Printing each term
    a, b = b, a + b    # Updating the terms for the next iteration


# Q6: Below is a Python program intended to print all prime numbers between 2 and 30. However, the code contains errors and does not function as expected. Identify the errors, explain what they are, and provide the corrected code.

# # Python program to print prime numbers between 2 and 30

# n = 30
# for num in range(2, n + 1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#         else:
#             print(num)
