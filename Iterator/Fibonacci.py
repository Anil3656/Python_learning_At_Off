class Fibonacci:
    def __init__(self,max_limit):
        self.a = 0
        self.b = 1
        self.max = max_limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b , self.a + self.b
        return value

fib = Fibonacci(10)
for num in fib:
    print(num)