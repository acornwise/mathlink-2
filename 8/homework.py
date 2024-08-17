def is_divisible(n, m):
    return (n / m) == (n // m)

def is_prime(n):
    for it in range(2, n):
        if n % it == 0:
            return True
    
    return False

def percent_to_decimal(p):
    return p * 0.01

def decimal_to_percentage(d):
    return round(d * 100)

def fraction_of_total(n, total):
    return n / total

print(is_divisible(6, 3))
print(is_prime(89))
print(percent_to_decimal(58))
print(decimal_to_percentage(0.58))
print(fraction_of_total(2, 5))
