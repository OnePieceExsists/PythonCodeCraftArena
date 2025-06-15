def sum_to_n(n):
    # Simple formula: n * (n + 1) // 2
    return n * (n + 1) // 2

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

