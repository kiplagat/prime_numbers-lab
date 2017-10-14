def prime_numbers(n):
	prime_numbers = []
	if n < 1:
		return []
	if isinstance(n, list):
		print("cannot be a list") 
	if isinstance(n, dict):
		print("cannot be dictionary") 
	else:
		for x in range(2,n):
			for i in range(2,x):
				if(x%i) == 0:
					break
			else:
				prime_numbers.append(x)
	return prime_numbers
