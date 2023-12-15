import unittest
import sys
sys.path.append('./')

from CryptoFunctions import*

class TestElGamal(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6, "GCD of 48 and 18 should be 6")
        self.assertEqual(gcd(0, 5), 5, "GCD of 0 and 5 should be 5")
        self.assertEqual(gcd(123456, 7890), 6, "GCD of 123456 and 7890 should be 6")
        large_num1 = 2**20  
        large_num2 = 2**18 
        self.assertEqual(gcd(large_num1, large_num2), large_num2, "GCD of 2^20 and 2^18 should be 2^18")

    def test_fast_exp(self):
        self.assertEqual(fast_exp(2, 3, 5), 3, "2^3 mod 5 should be 3")
        self.assertEqual(fast_exp(123456, 2, 100000), 83936, "123456^2 mod 100000 should be 83936")
        self.assertEqual(fast_exp(2, 20, 100), 76, "2^20 mod 100 should be 76")
        large_base = 2**10  
        large_exponent = 2**10  
        modulus = 2**10 + 1  
        self.assertEqual(fast_exp(large_base, large_exponent, modulus), 1, "1024^1024 mod 1025 should be 1")
    
    def test_exp_euclidean(self):
        gcd, x, y = exp_euclidean(30, 12)
        self.assertEqual(gcd, 6, "GCD of 30 and 12 should be 6")
        self.assertEqual(30 * x + 12 * y, 6, "Linear combination of 30 and 12 should result in their GCD")

        gcd, x, y = exp_euclidean(123456, 7890)
        self.assertEqual(gcd, 6, "GCD of 123456 and 7890 should be 6")
        self.assertEqual(123456 * x + 7890 * y, 6, "Linear combination of 123456 and 7890 should result in their GCD")

        large_num1 = 2**20  
        large_num2 = 2**18  
        gcd, x, y = exp_euclidean(large_num1, large_num2)
        self.assertEqual(gcd, large_num2, "GCD of 2^20 and 2^18 should be 2^18")
        self.assertEqual(large_num1 * x + large_num2 * y, large_num2, "Linear combination of 2^20 and 2^18 should result in their GCD")

        # Test with one zero input
        gcd, x, y = exp_euclidean(0, 5)
        self.assertEqual(gcd, 5, "GCD of 0 and 5 should be 5")
        self.assertEqual(0 * x + 5 * y, 5, "Linear combination of 0 and 5 should result in their GCD")

    def test_find_random_prime(self):
        prime = find_random_prime(8)
        self.assertTrue(is_prime(prime), "Number should be prime")
        self.assertTrue(2**7 <= prime < 2**8, "Prime should be 8-bit long")

        prime = find_random_prime(16)
        self.assertTrue(is_prime(prime), "Number should be prime")
        self.assertTrue(2**15 <= prime < 2**16, "Prime should be 16-bit long")

        prime = find_random_prime(32)
        self.assertTrue(is_prime(prime), "Number should be prime")
        self.assertTrue(2**31 <= prime < 2**32, "Prime should be 32-bit long")

        # Repeat test to check for different primes
        another_prime = find_random_prime(32)
        self.assertNotEqual(prime, another_prime, "Subsequent calls should generate different primes")

    def test_is_prime(self):
        self.assertTrue(is_prime(2), "2 should be prime")
        self.assertTrue(is_prime(17), "17 should be prime")

        self.assertFalse(is_prime(15), "15 should not be prime")

        self.assertTrue(is_prime(65537), "65537 should be prime")

        self.assertFalse(is_prime(65536), "65536 should not be prime")

        # Test edge cases
        self.assertFalse(is_prime(1), "1 should not be prime")
        self.assertFalse(is_prime(-13), "-13 should not be prime")
    
    def test_miller_rabin_test(self):

        self.assertTrue(miller_rabin_test(2, 3), "3 is a prime")
        self.assertTrue(miller_rabin_test(4, 7), "7 is a prime")

        self.assertTrue(miller_rabin_test(65536, 65537), "65537 is a prime")

        # Test for edge case
        self.assertFalse(miller_rabin_test(4, -7), "-7 is a prime")

        # List of known composite numbers
        composite_numbers = [8, 9, 10, 12, 15, 16, 18, 20, 21]

        for n in composite_numbers:
            # Decompose n - 1 as d * 2^r with d odd
            d = n - 1
            while d % 2 == 0:
                d //= 2

            # Ensure that d is initialized such that d * 2^r = n - 1
            # And also ensure that the loop in miller_rabin_test can terminate
            # Running Miller-Rabin test with a random base between 2 and n-2
            base = random.randint(2, n - 2)
            self.assertFalse(miller_rabin_test(base, n))

    def test_pollards_rho(self):

        self.assertEqual(pollards_rho(91), 7, "The smallest prime factor of 91 should be 7")

        self.assertIn(pollards_rho(10403), [101, 103], "The smallest prime factor of 10403 should be 101 or 103")

        self.assertTrue(pollards_rho(101) in [101, None], "Pollard's Rho should return the number itself or None for a prime number")

        large_composite = 2**16 + 1  
        self.assertTrue(pollards_rho(large_composite) in [None, large_composite], "Pollard's Rho should return None or the number itself for a large prime number")

    def test_prime_factors(self):
        self.assertEqual(prime_factors(101), [101], "Failed for prime number 101")
        self.assertEqual(prime_factors(28), [2, 2, 7], "Failed for composite number 28") 
        self.assertEqual(prime_factors(10403), [101, 103], "Failed for composite number 28")

    def test_is_primitive_root(self):
        # Test for know primes and primitive roots
        self.assertTrue((find_primitive_root(179), 2), "Failed for primitive prime")
        self.assertTrue((find_primitive_root(1009), 11), "Failed for primitive prime")
        self.assertTrue((find_primitive_root(4133), 2), "Failed for primitive prime")
        self.assertTrue((find_primitive_root(61469), 2), "Failed for primitive prime")

    def test_mod_inverse(self):

        self.assertEqual(mod_inverse(3, 11), 4, "Inverse of 3 modulo 11 should be 4")
        self.assertEqual(mod_inverse(10, 17), 12, "Inverse of 10 modulo 17 should be 12")

        self.assertEqual(mod_inverse(1234569, 9874321), 3717808, "Inverse of 123456789 modulo 987654321")

        self.assertEqual(mod_inverse(2, 5), 3, "Inverse of 2 modulo 5 should be 3")

    def test_baby_step_giant_step(self):
        g, h, p = 2, 5, 11
        expected = 4  # Because 2^4 % 11 = 5
        self.assertEqual(baby_step_giant_step(g, h, p), expected, "Failed for g=2, h=5, p=11")

        g, h, p = 3, 13, 17
        expected = 4  # Because 3^4 % 17 = 13
        self.assertEqual(baby_step_giant_step(g, h, p), expected, "Failed for g=3, h=13, p=17")

        # Test case where no solution exists
        g, h, p = 3, 8, 13
        self.assertIsNone(baby_step_giant_step(g, h, p), "Should return None for g=3, h=8, p=13 with no solution")

# Commentting out to run coverage.py for complete test coverage        
# if __name__ == '__main__':
#     unittest.main()