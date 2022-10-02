age =int(input("Enter the age: "))

if age >= 18:
	print("You are eligible to vote")
elif age <= 0:
	print("you are not born",)
else:
	print("You are not eligible to vote",age)
print("Done\n")
