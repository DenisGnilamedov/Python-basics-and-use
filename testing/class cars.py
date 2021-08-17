class Machine:
    def __init__(self, n, m, v):
        self.n = n
        self.m = m
        self.v = v
        self.abs = False

    def turn_on_abs(self):
        if self.has_abs():
            self.abs = True

    def has_abs(self):
        return True

    def print_params(self):
        print(self.n, self.m, self.v)


class BMW(Machine):
    def init(self, n, m, v):
        super().__init__(n, m, v)

    def ac(self):
        print('I have a AC')


class Lada(Machine):
    def init(self, n, m, v):
        super().__init__(n, m, v)


bmw = BMW('BMW', 'm6', 4.2)
zhigule = Lada('Vaz', 'priora', 1.5)

bmw.print_params()
zhigule.print_params()

bmw.ac()
zhigule.ac()