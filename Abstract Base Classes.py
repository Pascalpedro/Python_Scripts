class MyAbsClass:
    pass


class MyConcreteClass(MyAbsClass):
    @property

    def myproperty(self):
        return 42

    def mymethod(self, value):
        assert 42 == 42


c = MyConcreteClass()
print(c.myproperty)
