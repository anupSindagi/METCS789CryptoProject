import unittest
import sys
sys.path.append('./')

from RSA import*

class TestRSA(unittest.TestCase):

    def test_key_generation(self):
        public_key, private_key = generate_rsa_keys()
        p,q = prime_factors(public_key[1])
        phi = (p - 1) * (q - 1)
        # Check if e and d satisfy e * d ≡ 1 (mod φ(n))
        self.assertEqual((public_key[0] * private_key[0]) % phi, 1)

        # Check if n is the product of two distinct primes
        self.assertNotEqual(p, q)
        self.assertEqual(public_key[1], p * q)

        # Check in case p and q are equal
        public_key, private_key = generate_rsa_keys(2) # 2 bit to result in equal in p and q
        p,q = prime_factors(public_key[1])
        self.assertNotEqual(p, q)
        self.assertEqual(public_key[1], p * q)

    def test_rsa_encryption_decryption(self):
        public_key, private_key = generate_rsa_keys()  
        original_message = 1123123

        encrypted_message = encrypt_rsa(original_message, public_key)
        decrypted_message = decrypt_rsa(encrypted_message, private_key)

        self.assertEqual(original_message, decrypted_message)

    def test_rsa_interception(self):
        public_key, _ = generate_rsa_keys()  
        original_message = 123123123

        encrypted_message = encrypt_rsa(original_message, public_key)
        intercepted_message = intercept_rsa(encrypted_message, public_key)

        self.assertEqual(original_message, intercepted_message)

        # Check if a prime is given in place of n (p*q) it should return None
        p,_ = prime_factors(public_key[1])
        print(public_key[0],p)
        intercepted_message = intercept_rsa(encrypted_message, (public_key[0], p))
        self.assertEqual(intercepted_message, None)
        
# Commentting out to run coverage.py for complete test coverage     
# if __name__ == '__main__':
#     unittest.main()