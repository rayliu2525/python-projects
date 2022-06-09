class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if is_integer(self.capacity) == False or self.capacity < 0:
            raise ValueErrors
        self.cookies = 0

    def __str__(self):
        ...

    def deposit(self, n):
        self.cookies += n
        if n > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.cookies -+ n
        if n < 0:
            raise ValueError

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        ...