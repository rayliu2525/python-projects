class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if is_integer(self.capacity) == False or self.capacity < 0:
            raise ValueErrors

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...