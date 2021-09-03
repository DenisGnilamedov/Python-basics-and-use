class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable    # iterable - исходная последовательность
        self.funcs = funcs  # funcs - допускающие функции
        self.judge = judge  # judge - решающая функция

    def __iter__(self):
        for i in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs: # пробегаем по функциям (mul2,3,5), если истина - pos+=1
                if func(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg): # сравниваем pos и neg в каждой итерации, если удовлетворяет условиям judge, добавляем элемент в print.
                yield i


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]
print(list(multifilter(a, mul2, mul3, mul5)))





