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
		p = random.getrandbits(30)
	
	return p

# Generate p and q to get n = pq
def p_and_q():
	key = generate_good_primes(2) * generate_good_primes(2)
	
	

	return key

# Euclidean algorithm to find greatest common divisor of a, b
def gcd(a, b): 
	
	if a == 0 :
		return b 
	  
	return gcd(b%a, a)

# Seed Generation
def seed_generate():
	global number
	number = p_and_q()
	seed = 0
	while not gcd(number, seed) == 1: 
		seed = random.randrange(1, number - 1)
	return seed

# Blum – Blum – Shub Random Number Generator
def blum_blum_shub(bit):
	s0 = seed_generate()
	bit_output = ""
	for _ in range(bit):
		s0 = pow(s0, 2, number)
		b = s0 % 2
		bit_output += str(b)

	return int(bit_output,2)

# Generate keys for Elgamal encryption/decryption, p is the Group, g is generator, private key and public key
def el_gamal_key_generation(bit):
	p = blum_blum_shub(bit)
	while not mutiple_miller_iteraion(p):
		p = blum_blum_shub(bit)
	g = blum_blum_shub(bit)
	while not (1 < g < p-1 and gcd(p, g)==1):
		g = g = blum_blum_shub(bit)
	secrect_key = blum_blum_shub(bit)
	while not (1 < secrect_key < p-1):
		secrect_key = blum_blum_shub(bit)
	B = pow(g, secrect_key, p)
	return "P:",p, " g:", g, " private key:",secrect_key, "public key:",B

print(el_gamal_key_generation(25))