Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def primality_checker():
	number = int(input("Enter a number: "))
	divisors = []
	for i in range(1,number+1):
		if number%i==0:
			divisors.append(i)
	if len(divisors)==2:
		print(str(number) + " is a prime number.")
	else:
		print(str(number) + " is not a prime number.")