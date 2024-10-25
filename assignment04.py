

# Dated: Thurs, Oct 24, 2024		         Due: Sat, Oct 26, 2024 : 11:59 PM

# PYTHON FOR MATHEMATICIANS
# Assignment # 4
# Ask for the user’s first name and display the output message Hello [First Name].

name = input("Enter your name: ")
print(f'Hello, {name}')

# Ask for the user’s first name and then ask for their surname and display the output message Hello [First Name] [Surname].
name = input("Enter your name: ")
surname = input("Enter your surname: ")
print(f'Hello, {name} {surname}')

# Write code that will display the joke “what do you call a bear with no teeth?” and on the next line display the answer “A gummy bear!” Try to create it using only one line of code.

print("What do you call a bear with no teeth?\nA gummy bear!")

# Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer].

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

sum = (num1 + num2)
answer = sum * num3
print(f'The answer is {answer}')

# Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age].
name = input("Enter your name: ")
age = int(input("Enter your age: "))

new_age = age+1
print(f'{name} next birthday you will be {new_age}')

# Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
days = int(input("Enter number of days: "))


hours = days * 24
minutes = hours * 60
seconds = minutes * 60


print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
# Ask the user to enter their first name and surname is lower case. Change the case to title case and join them together. Display the finished result.
first_name = input("Enter your first name in lowercase: ").title()
surname = input("Enter your surname in lowercase: ").title()
full_name = " ".join([first_name, surname])
print("Full name:", full_name)

# Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a string number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1).
rhyme = input("Enter first line of rhyme: ")
print(len(rhyme))
starting_num = int(input("Enter starting num: "))
ending_num= int(input("Enter ending num: "))
print(rhyme[starting_num:ending_num+1])


# Ask the user to type in any word and display it in upper case.

any_word = input("Enter any word: ")
print(any_word.upper())

# Write a Python function that takes a string and returns the string reversed.
s = "Hello"
reversed_str = s[::-1]
print(reversed_str)  


