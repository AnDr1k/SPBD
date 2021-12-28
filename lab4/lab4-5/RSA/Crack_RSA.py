import math
from extended_euclidean import gcd_extended
# Fermat factor to factor n = p * q
def fermat_factor(n):
    if(n<= 0):
        return [n] 
 
    # check if n is even 
    if(n & 1) == 0: 
        return [n / 2, 2]
         
    a = math.ceil(math.sqrt(n))
 
    if(a * a == n):
        return [a, a]
    
    # Geting p and q
    while(True):
        b1 = a * a - n
        b = int(math.sqrt(b1))
        if(b * b == b1):
            break
        else:
            a += 1
    return [a-b, a + b]

# Calculate private key by using p and q to get phi(n), then calculate multiplicative inverse of public key E to get private key. 
def crack_rsa(n, E, cipher):
    p, q = fermat_factor(n)
    print("p:", p,"q:",q)
    phi = (p-1)*(q-1)
    g, x, y = gcd_extended(E, phi)
    if x < 0:
        x = x % phi
        D = x
        return pow(cipher, D, n)
    else:
        D = x
        return pow(cipher, D, n)
    
#crack_rsa(N, public key, cipher)
print(crack_rsa(1230043, 281929, 660754))
print(crack_rsa(8638613 , 1523917, 3279901))