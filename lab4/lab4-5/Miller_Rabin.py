import random

# Single iteration of miller Rabin test to check a number is prime or not
def miller_primality_test(n, b):
	e = n-1
	while not e % 2 == 0:
		e //= 2

	if pow(b, e, n) == 1:
		return True

	while e < n-1:
		if pow(b,e,n) == n-1:
			return True

		e = e*2
	return False

# k times Miller Rabin iteration to check isprime
def mutiple_miller_iteraion(n):
	k = 10
	for _ in range(k):
		b = random.randrange(2, n - 1)
		if not miller_primality_test(n, b):
			return False
		
	return True

n = int(input(" : "))
print(mutiple_miller_iteraion(n))