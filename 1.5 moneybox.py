class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if v <= self.capacity:
            return True
        else:
            return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        self.can_add(v)
        self.capacity -= v
        # положить v монет в копилку

x = MoneyBox(15)
x.add(16)
x.add(9)
x.add(3)