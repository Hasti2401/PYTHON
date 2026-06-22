class Calculator():

    def add (self, a,b):
        print(a + b)
    
    def _sub(self,a,b):
        print(a - b)
    
    def __mull(self,a,b):
        print(a * b)

    def show(self):
        self.__mull(10, 5)

c = Calculator()

c.add(10,5)

c._sub(10,5)

c.show()