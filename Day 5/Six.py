class ParentClass():

    def func1(self):
        print("Parenr Method Called")


class ChildClass(ParentClass):

    def func1(self):
        print("Child method Called")


c = ChildClass()
c.func1()
