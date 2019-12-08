print("Input your age below to see if you are eligible to vote\n")

# user inputs the age they want to check
age = int(input("Enter Age: "))

# conditional statement checks whether the number input is >= 18
if age >= 18:
    print("\nCongrats! You are eligible to vote as you are old enough.")
else:
    print("\nSorry, you are not eligible to vote as you are not old enough.")