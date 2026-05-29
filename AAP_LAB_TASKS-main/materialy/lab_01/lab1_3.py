# TODO: Implementacja generatora liczb pierwszych
def prime_generator():
    yield 2
    
    candidate = 3
    while True:
        is_prime = True
        for i in range(3, int(candidate**0.5) + 1, 2):
            if candidate % i == 0:
                is_prime = False
                break
                
        if is_prime:
            yield candidate
            
        candidate += 2

primes_ending_in_9 = (p for p in prime_generator() if p % 10 == 9)

#Testowa funkcja
print("Kolejne 8 liczb pierwszych kończących się na 9:")
for _ in range(8):
    print(next(primes_ending_in_9))