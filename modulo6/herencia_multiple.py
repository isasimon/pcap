class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A, B):
    pass


d = D()