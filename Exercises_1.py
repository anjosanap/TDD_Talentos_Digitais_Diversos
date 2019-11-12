## enter a number and print weither it's odd or even

number = int(input("Enter a whole number: "))

rest = number % 2

if rest == 0:
    print("Number is even!")
else:
    print("Number is odd!")
