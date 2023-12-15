import random

from CryptoFunctions import*

def generate_rsa_keys(bit_length=24):
    p = find_random_prime(bit_length)
    q = find_random_prime(bit_length)
    while p == q:
        q = find_random_prime(bit_length)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    gcd, d, _ = exp_euclidean(e, phi)
    while gcd != 1:
        e = random.randrange(1, phi)
        gcd, d, _ = exp_euclidean(e, phi)

    d = d % phi if d < 0 else d
    return (e, n), (d, n)

def encrypt_rsa(message, public_key):
    e, n = public_key
    return fast_exp(message, e, n)

def decrypt_rsa(encrypted_message, private_key):
    d, n = private_key
    return fast_exp(encrypted_message, d, n)

def intercept_rsa(encrypted_message, public_key):
    e, n = public_key
    factor = pollards_rho(n)
    if factor == n or factor == None:
        return None  # Failed to factorize
    phi = (factor - 1) * (n // factor - 1)
    _, d, _ = exp_euclidean(e, phi)
    d = d % phi if d < 0 else d
    return fast_exp(encrypted_message, d, n)



