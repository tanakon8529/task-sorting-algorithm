def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_prime_numbers(n):
    return sum(i for i in range(2, n+1) if is_prime(i))

if __name__ == "__main__":
    print(sum_prime_numbers(4))
    print(sum_prime_numbers(5))
    print(sum_prime_numbers(15))
