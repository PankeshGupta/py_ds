class stack:
    def __init__(self,data_quantity):
        self.stk = []
        self.limit = data_quantity
    def push(self,data):
        if len(self.stk) >= self.limit :
            print("stack overflow")
        else:
            self.stk.append(data)
    def pop(self):
        if len(self.stk) == 0 :
            print("stack underflow")
        else:
            print(self.stk.pop())
    def travel(self):
        for i in self.stk:
            print("the data is ",i)

    
