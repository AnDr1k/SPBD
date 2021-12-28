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
def blum_blum_shub():
	s0 = seed_generate()
	bit_output = ""
	for _ in range(30):
		s0 = pow(s0, 2, number)
		b = s0 % 2
		bit_output += str(b)

	
	return int(bit_output,2)

# Extened Euclidean to calcute multiplicative inverse
def gcd_extended(a, b): 
    if a == 0 :  
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b%a, a) 
     
    x = y1 - (b//a) * x1 
    y = x1 
    return gcd, x, y

# RSA key generation. Generate two random prime number p and q by blum_blum_shub and Miller Rabin algorithm. 
# Calculate N = pq and phi = (p-1)(q-1), generate public key by BBS, calculate multiplicative inverse of private key by extended Euclidean.
def key_generation():
	p = blum_blum_shub()
	q = blum_blum_shub()
	while not mutiple_miller_iteraion(p):
		p = blum_blum_shub()
	while not mutiple_miller_iteraion(q):
		q = blum_blum_shub()
	N = p * q
	L = (p - 1) * (q - 1)
	E = blum_blum_shub()
	while not (gcd(E, L) and 1<E<L):
		E = blum_blum_shub()
	g, x, y = gcd_extended(E, L)
	D = x
	if D < 0:
		D = D % L
		return ("p：", p ,"q:", q, "N: ", N, "phi:",L, "public key:",E, "private key:",D )
	else:
		return ("p：", p ,"q:", q, "N: ", N, "phi:",L, "public key:",E, "private key:",D )



print(key_generation())
