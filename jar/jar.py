class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if not isinstance(self._capacity, int) or self._capacity < 0:
            raise ValueErrors
        self.cookies = 0

    def __str__(self):
        return {self.size} * "🍪"

    def deposit(self, n):
        self.cookies += n
        if n > self._capacity:
            raise ValueError

    def withdraw(self, n):
        self.cookies -= n
        if n < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

jar = Jar()
jar.deposit(2)
print(jar)
