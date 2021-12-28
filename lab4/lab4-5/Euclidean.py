a = int(input('Enter a:' ))
b = int(input('Enter b:' ))

def gcd(a, b): 
    print(b, a)
    if a == 0 :
        return b 
      
    return gcd(b%a, a)
    
print("gcd(", a , "," , b, ") = ", gcd(a, b))