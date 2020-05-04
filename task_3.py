"""
Write a program that reads an integer number and prints its previous and
next numbers. See the examples below for the exact format your answers
should take. There shouldn't be a space before the period.
Remember that you can convert the numbers to strings using the function str.
The next number for the number 179 is 180. The previous number for the number 179 is 178.)

"""
number = 'string'
while type(number) != int:
        a = input("Enter your number here:") 
        if a.isdigit() == True:
            number = int(a)
        else:  
            print("Enter only numbers without space")

print(f"Your number is {number}. \nPrevious number of your number is {number -1}. \nAnd next number of your number is {number + 1}")

