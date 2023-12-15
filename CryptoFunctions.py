import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fast_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def exp_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = exp_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_random_prime(n):
    while True:
        p = random.randrange(2**(n-1), 2**n)
        if is_prime(p):
            return p

def is_prime(n, k=128):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True

def miller_rabin_test(d, n):
    # Handling the trivial cases first
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Find d such that d * 2^r = n - 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(5):  # Repeat the test 5 times for more accuracy
        a = random.randint(2, n - 2)
        x = fast_exp(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False

    return True

def pollards_rho(n):
    
    if n % 2 == 0:
        return 2

    # The function f(x) = (x^2 + 1) mod n
    def f(x):
        return (x*x + 1) % n

    x, y, d = 2, 2, 1

    # Using Floyd's cycle-finding algorithm
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    # This check is to see if we've found a non-trivial factor
    if d != n:
        return d
    else:
        return None


def prime_factors(n):
    
    factors = []
    while pollards_rho(n) is not None:
        # print(n, pollards_rho(n))
        factors.append(pollards_rho(n))
        n = n//pollards_rho(n)
    factors.append((n))
    return factors


def is_primitive_root(g, p):
    phi = p - 1
    factors = set(prime_factors(phi))
    for factor in factors:
        if pow(g, phi // factor, p) == 1:
            return False
    return True

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g


def mod_inverse(a, m):
    
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def baby_step_giant_step(g, h, p):
    m = int(p ** 0.5) + 1

    # Baby steps - compute g^j for all j in [0, m-1]
    baby_steps = {pow(g, j, p): j for j in range(m)}

    # Giant steps - compute h * g^(-im) for all i in [0, m-1]
    inv_g_m = pow(g, -m, p)  # g^(-m)
    giant_step = h
    for i in range(m):
        if giant_step in baby_steps:
            return i * m + baby_steps[giant_step]
        giant_step = (giant_step * inv_g_m) % p

    return None  






