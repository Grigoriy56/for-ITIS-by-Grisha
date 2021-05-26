class A():
    def __init__(self):
        self. x = 3

class C(A):
    def __init__(self):
        self.x = 4

class B(A, C):
    pass

c = B
print(c.x)