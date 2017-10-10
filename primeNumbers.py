for prime_numbers in range(1,101):
    prime = True
    for i in range(2,prime_numbers):
      if (prime_numbers%i==0):
         prime = False
    if prime:
       print(prime_numbers)  
	
  
  
  
