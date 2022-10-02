number = 19
print("****Starting The Game****")
while True:
	guess = int(input("Enter an integer: "))
	if guess == number:
		print("Congratulations you guessed it :)")
		print("****End of The Game****")
		break;

	elif guess<number:
		print("Nope, Try a bit higher :( \n")

	else:
		 print("No, Try a bit lower :( \n")
