def primality_checker():
	number = int(input("Enter a number: "))
	divisors = []
	for i in range(1,number+1):
		if number%i==0:
			divisors.append(i)
	if len(divisors)==2:
		print(str(number) + " is a prime number.")
	else:
		print(str(number) + " is not a prime number.")
