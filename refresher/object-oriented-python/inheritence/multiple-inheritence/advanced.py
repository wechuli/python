class A:
    def do_something(self):
        print("Method defined in: A")


class B(A):
    def do_something(self):
        print("Method defined in: B")


class C(A):
    def do_something(self):
        print("Method defined in: C")


class D(B, C):
    pass

    def do_something(self):
        print("Method defined in: D")
        super().do_something() #super calls in the function in the Method Resolution Order


# print(help(D))
# print(D.mro())
# print(D.__mro__)
multi = D()
multi.do_something()
