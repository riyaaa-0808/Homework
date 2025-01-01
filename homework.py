
'''#write a program that ask a user to enter the number and checks whether the number is multiple of 10
num=int(input("Enter the number : "))
if num%10 == 0 :
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of 10")

    #write a program that ask the user to enter their age and check if they are eligible to vote(age 18 or older).
    age = int(input("Enter your age: "))
    if age >=18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

#write the python program that ask the user to enter their marks and check if they passed or fail.
marks = float(input("Enter your marks: "))
if marks >=40:
    print("YAY! you passed your exam")
else:
    print("Sorry,you need to work hard")'''

    #write a python program that takes two number as input and print whether the first number is greater, less than, or equal to the rest of the number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
        print(f" {num1} is greater than {num2}.")
elif num2 > num1:
    print(f" {num1} is less than {num2}.")
else:
    print(f" {num1} and {num2} are equal.")

#write a python program that ask the user to enter a year and check whether it is leap year or not.
year = int(input("Enter a year: "))
if(year %  400 == 0 ) and (year % 100 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")

