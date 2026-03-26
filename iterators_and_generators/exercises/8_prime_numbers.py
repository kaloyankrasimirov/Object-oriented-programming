def get_primes(my_list:list):
    for n in my_list:
        def is_prime(num):
            return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
        if is_prime(n):
            yield n

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))