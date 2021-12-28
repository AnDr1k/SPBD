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

# To check future generated p = 3 mod 4 and q = 3 mod 4
def generate_good_primes(p):
	while not (p % 4 == 3 and mutiple_miller_iteraion(p)):
		p = random.getrandbits(15)
	print(p)
	return p

# Generate p and q to get n = pq
def p_and_q():
	key = generate_good_primes(2) * generate_good_primes(2)
	
	print("n is :",key)

	return key

# Euclidean algorithm to find greatest common divisor of a, b
def gcd(a, b): 
    
    if a == 0 :
        return b 
      
    return gcd(b%a, a)

# Seed Generation
def seed_generate():
	global n
	n = p_and_q()
	seed = 0
	while not gcd(n, seed) == 1: 
		seed = random.randrange(1, n - 1)
	return seed

# Blum – Blum – Shub Random Number Generator
def blum_blum_shub(bit):
	s0 = seed_generate()
	bit_output = ""
	for _ in range(bit):
		s0 = pow(s0, 2, n)
		b = s0 % 2
		bit_output += str(b)

	print(bit_output)
	return int(bit_output,2)


print(blum_blum_shub(30))


	
