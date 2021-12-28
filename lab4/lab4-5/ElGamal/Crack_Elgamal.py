from math import ceil, sqrt

# Baby step giant step to calculate Log(b)a in numer p where b is generator, a is the public key from Alice or Bob, p is the group. Then the result will be Alice's or Bob's private key.

# Baby step giant step
def bsgs(b, a, p):
    
    #ceiling of m by determine the square root of p-1, and we will round it up to the nearest integer
    m = ceil(sqrt(p - 1))  

    # Baby step
    tbl = {pow(b, i, p): i for i in range(m)}
    
    # Fermat’s Little Theorem
    c = pow(b, m * (p - 2), p)

    for j in range(m):
        y = (a * pow(c, j, p)) % p
        if y in tbl:
            return j * m + tbl[y]
    return None

# Extened Euclidean to calcute multiplicative inverse
def gcd_extended(a, b): 
    if a == 0 :  
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b%a, a) 
    
    x = y1 - (b//a) * x1 
    y = x1 
    return gcd, x, y

# By using baby step giant step we can find result for discret log which can figure out the private for both Bob and Alice
def crack_elgamal(generator, A, B, p, ciper):
    private_a = bsgs(generator, A, p)
    private_b = bsgs(generator, B, p)
    x1 = pow(A, private_b, p) 
    g, x, y = gcd_extended(x1, p)
    if x < 0:
        x = x % p
        plain = x * ciper % p
        return ("Alice private key:",private_a, "Bob's private key:",private_b, 'Message is: ',plain)
    else: 
        plain = x * ciper % p
        return ("Alice private key:",private_a, "Bob's private key:",private_b, 'Message is: ',plain)

# crack_elgamal(generator, publice key from Alice, Public key from Bob, group p, ciper):
print(crack_elgamal(541239,845216,680806, 890231, 246520))
print(crack_elgamal(5,17517503,10791381, 33432023, 20208430708))