number = input("Enter a number: ") # user input stored in variable number

number = int(number)

print("The numbered entered was", number)

if (number % 2) == 0:	# check if the number devided by 2 will have a remainder
	print("That is an even number")
else:
	print("That is an odd number")
if (number % 10) == 0:
	print("The number is divisible by 10")
else:
	print("The number is not divisible by 10")
