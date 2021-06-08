class ParentClass():

    def func1(self):
        print("Parent method called")


class ChildClass(ParentClass):

    def func1(self):
        print("Child method called")


c = ChildClass()
c.func1()


p = ParentClass()
p.func1()
