encrypt_decrypt = input("Encrypt or Decrypt: (e/d)")
exp = int(input("Enter the exponent: "))
m = int(input("Enter the N: "))

# Function for RSA encryption. exp is public key in this case. m is N=pq
def rsa_encryption(exp, m):
    p = int(input("Enter the plaintxt to encrypt: "))
    c = pow(p, exp, m)
    print("Ciper is: ", c)
    
# Function for RSA decryption. exp is private key in this case. m is N = pq
def rsa_decryption(exp, m):
    c = int(input("Enter the ciper to decrypt: "))
    p = pow(c, exp, m)
    print("Plaintext is: ", p)


def en_de():
    if (encrypt_decrypt == 'e'):
        rsa_encryption(exp, m)
    elif (encrypt_decrypt == 'd'):
        rsa_decryption(exp, m)
    else:
        print("not a valid input")

en_de()