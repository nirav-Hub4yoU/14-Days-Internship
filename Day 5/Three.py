class Myclass():
    n1 = 0
    n2 = 0

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def func1(self):
        ans = self.n1+self.n2
        print('Ans is :', ans)


myc = Myclass(50, 79)
myc.func1()
