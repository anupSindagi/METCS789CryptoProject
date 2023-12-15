import random

from CryptoFunctions import*

def generate_keys(bit_length=24):
    p = find_random_prime(bit_length) 
    g = find_primitive_root(p)
    x = random.randrange(1, p)
    h = pow(g, x, p)
    return (p, g, h), x

def encrypt_elgamal(message, public_key):
    p, g, h = public_key
    k = random.randrange(1, p)
    c1 = pow(g, k, p)
    c2 = (message * pow(h, k, p)) % p
    return c1, c2

def decrypt_elgamal(ciphertext, private_key, p):
    c1, c2 = ciphertext
    s = pow(c1, private_key, p)
    s_inv = mod_inverse(s, p)
    return (c2 * s_inv) % p

def intercept_elgamal(public_key, ciphertext):
    p, g, h = public_key
    c1, c2 = ciphertext

    # Find the secret key x using Baby-Step Giant-Step
    x = baby_step_giant_step(g, h, p)
    if x is None:
        return None  

    # Decrypt the message using the found secret key
    s = pow(c1, x, p)
    s_inv = mod_inverse(s, p)
    message = (c2 * s_inv) % p
    return message


