p = 11 #prime
q =13 #prime 
n = p * q 
phi = (p-1)*(q-1) #totient
e = 7
def gcd(a, b): #greatest common divisor
    while b != 0:
        a, b = b, a % b
    return a
def modinv(a, m): #modular inverse
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

d = modinv(e, phi) #private key exponent

def encrypt(plaintext): #encryption function
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(ciphertext):# decryption function
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

if __name__ == "__main__":
    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(message)
    print("Encrypted:", encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg)
    print("Decrypted:", decrypted_msg)