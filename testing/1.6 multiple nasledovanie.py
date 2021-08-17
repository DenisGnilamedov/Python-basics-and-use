class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C) : pass

# используем issubclass , чтобы понять для 2 классов, кто является предком кого
# 2 аргумента: проверяет, что первый аргумент является наследником второго
issubclass(A, A) # True
issubclass(C, D) # False
issubclass(A, D) # True
issubclass(C, object) # True
issubclass(object, C) # False
# isinstance позволяет узнать, ведет-ли себя объект как экземпляр какого-либо класса
# создаем экземпляр класса А - x
x = A()
isinstance(x, A) # True
isinstance(x, B) # True
isinstance(x, object) # True
isinstance(x, str) # False

# MRO - порядок разрешения методов:
print(A.mro())
