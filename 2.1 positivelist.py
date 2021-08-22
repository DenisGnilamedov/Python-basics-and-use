class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, x):
        if x > 0:
            list.append(self, x)
        else:
            raise NonPositiveError

lst = PositiveList([])
lst.append(0)

print(lst)