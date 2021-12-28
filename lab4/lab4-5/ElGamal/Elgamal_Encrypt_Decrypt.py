import random


encrypt_decrypt = input("El Gamal Encrption/Decryption(e/d): ")
p = int(input("Enter group p: "))

# Miller Rabin test to test if a number is prime.
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

# Miller Rabin 
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

# Function for encryption, p is group, g is generator and B is public key From Bob
def elgmal_encrypt(p, g, B):
	plain = int(input("Enter plain to encrypt: "))
	k = blum_blum_shub(30)
	while not 1 < k < p:
		k = blum_blum_shub(30)
	A = pow(g, k, p)
	ciper = plain * pow(B, k, p)
	print("g:",g,"public key:", A, "key:",k, "ciper:",ciper)

# Extened Euclidean to calcute multiplicative inverse
def gcd_extended(a, b): 
	if a == 0 :  
		return b, 0, 1
	gcd, x1, y1 = gcd_extended(b%a, a) 
	 
	x = y1 - (b//a) * x1 
	y = x1 
	return gcd, x, y

# Function for decryption, p is group, sec is Bob private key and A is public key from Alice
def elgamal_decrypt(p, sec, A):
	ciper = int(input("Enter number to decrypt:"))
	x1 = pow(A, sec, p) 
	g, x, y = gcd_extended(x1, p)
	invese = x
	plain = invese * ciper % p
	print("Plain text is: ", plain)
	
	
# Function to encryption/decryption
def en_de():
	
	
	if (encrypt_decrypt == 'e'):
		B = int(input("Enter public key from other: "))
		g = int(input("Enter generator: "))
		elgmal_encrypt(p, g, B)
	elif (encrypt_decrypt == 'd'):
		A = int(input("Enter public key from other: "))
		sec = int(input("Enter secrect key: "))
		elgamal_decrypt(p, sec, A)
	else:
		print("not a valid input")


en_de()