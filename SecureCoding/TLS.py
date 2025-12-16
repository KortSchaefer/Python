'''
TLS.py

This proram will emulate a TLS handshake which HTTPS uses to securly transfer data between a client and server.
It will use RSA asymmetric encryption to securely exchange a symmetric key, then use that symmetric key to encrypt and decrypt data using AES.
This method combines the security of asymmetric encryption with the efficiency of symmetric encryption, and allows for secure data transfer over an insecure channel.

Author: Kort Schaefer
Date: 11/10/2025
'''

import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

#=========================
#Emulate Server Startup
#=========================

def generate_rsa_keypair():
    #built in function to generate RSA keypair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key() #key generation
    
    return private_key, public_key

server_private_key, server_public_key = generate_rsa_keypair() #generate keypair in scope of server

#=========================
#TLS Handshake Emulation
#=========================

def client_generate_symetric_key():
    return AESGCM.generate_key(bit_length=128) #generate symmetric key for AES

def client_encrypt_symmetric_key(symmetric_key, server_public_key): #encrypt symmetric key with server's public key
    encrypted_key = server_public_key.encrypt( #encrypt
        symmetric_key,
        padding.OAEP( #Optimal Asymmetric Encryption Padding
            mgf=padding.MGF1(algorithm=hashes.SHA256()), #mask generation function with SHA256
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_key

#=========================
#server decrypts symmetric key
#=========================

def server_decrypt_symmetric_key(encrypted_key, server_private_key):
    symmetric_key = server_private_key.decrypt( #decrypt
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return symmetric_key

#=========================
#AES-GCM Data Encryption/Decryption (symmetric)
#=========================

def encrypt_data(data, symmetric_key): #encrypt data with symmetric key
    cipher = AESGCM(symmetric_key) #create AESGCM cipher object
    nonce = os.urandom(12) #generate random nonce/salt
    ciphertext = cipher.encrypt(nonce, data, None) #encrypt data with AESGCM cipher
    return nonce, ciphertext #return nonce/salt and ciphertext
def decrypt_data(nonce, ciphertext, symmetric_key): #decrypt data with symmetric key
    cipher = AESGCM(symmetric_key) #create AESGCM cipher object
    plaintext = cipher.decrypt(nonce, ciphertext, None) #decrypt data with AESGCM cipher
    return plaintext #return plaintext

'''
Program Execution Flow
1. Server generates RSA keypair on startup.
2. Client generates symmetric key.
3. Client encrypts symmetric key with server's public key.
4. Server decrypts symmetric key with server's private key.
5. Client encrypts data with symmetric key.
6. Server decrypts data with symmetric key.
'''

def simulate_tls_handshake_and_data_transfer():
    # Client Side
    symmetric_key = client_generate_symetric_key() #step 2
    print("\nSymmetric Key Generated Successfully:", symmetric_key)
    encrypted_symmetric_key = client_encrypt_symmetric_key(symmetric_key, server_public_key) #step 3
    print("\nSymmetric Key Encrypted Successfully: ", encrypted_symmetric_key)

    # Server Side
    decrypted_symmetric_key = server_decrypt_symmetric_key(encrypted_symmetric_key, server_private_key) #step 4
    print("\nSymmetric Key Decrypted Successfully:", decrypted_symmetric_key == symmetric_key)

    # Data Transfer
    print("\n--- Data Transfer ---")
    data_to_send_literal = input("Enter data to send: ") #data to be sent
    print("----- + ------\n")
    data_to_send = data_to_send_literal.encode() #encode data to bytes

    nonce, encrypted_data = encrypt_data(data_to_send, decrypted_symmetric_key) #step 5
    
    # Server decrypts the data
    decrypted_data = decrypt_data(nonce, encrypted_data, decrypted_symmetric_key) #step 6
    

    print("Original Data:", data_to_send, "\n")
    print("Symetric Data Encrypted Successfully: ", encrypted_data, "\n")
    print("Decrypted Data:", decrypted_data, "\n")

if __name__ == "__main__":
    simulate_tls_handshake_and_data_transfer()