class SayName:
    def __init__(self, name: str, **kwds):
        self.name = name
        super().__init__(**kwds)

    def sayName(self):
        print(f"my name is {self.name}")

class PrintAge:
    def __init__(self, age: int, **kwds):
        self.age = age
        super().__init__(**kwds)
    def printAge(self):
        print(f"I'm {self.age} years old")

class Test(PrintAge, SayName):
    def __init__(self, **kwds):
        super().__init__(**kwds)
    def test(self):
        self.sayName()
        self.printAge()

test = Test(name="Julian", age=3)
test.test()