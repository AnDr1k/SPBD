from math import ceil, sqrt

b = int(input("Enter b: "))
a = int(input("Enter a: "))
p = int(input("Enter p: "))

# Baby step giant step
def bsgs(b, a, p):
    #ceiling of m by determine the square root of p-1, and we will round it up to the nearest integer
    m = ceil(sqrt(p - 1))  
    print("Ceiling of sqrt m is: ", m)

    # Baby step
    tbl = {pow(b, i, p): i for i in range(m)}
    print(tbl)
    
    # Fermat’s Little Theorem
    c = pow(b, m * (p - 2), p)
    
    # Generate 
    for j in range(m):
        y = (a * pow(c, j, p)) % p
        if y in tbl:
            return j * m + tbl[y]
    return None


print("\nx = ", bsgs(b, a, p))