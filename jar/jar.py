class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self._capacity < (self.cookies + n):
            raise ValueError
        self.cookies += n

    def withdraw(self, n):
        if self.cookies < n:
            raise ValueError
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies