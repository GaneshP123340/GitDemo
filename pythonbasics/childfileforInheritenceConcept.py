from listdemo import calculator


class childimpl(calculator):
    num1 = 200

    def __init__(self):
        calculator.__init__(self , 2 ,99)

    def getcompletedata(self):
        return self.num1 + self.num + self.summation()


obj = childimpl()
print(obj.getcompletedata())
