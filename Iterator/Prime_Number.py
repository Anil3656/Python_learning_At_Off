class PrimeNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2  # Start from the first prime number

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.limit:
            num = self.current
            self.current += 1
            if self.is_prime(num):
                return num
        raise StopIteration

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

prime = PrimeNumbers(20)
for num in prime:
    print(num)