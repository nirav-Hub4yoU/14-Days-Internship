# inheritance Example
class Parent():
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method   ")

        # define class child


class Child(Parent):
    def __init__(self):
        print("Calling the Constructor")

    def childMethod(self):
        print("Calling Child method")


c = Child()
c.childMethod()
c.parentMethod()
