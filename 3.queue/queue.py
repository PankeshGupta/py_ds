# queues work on the principle of fifo , that means first in first out 
# elements are added at the end of the queue and removed fom the front
class q:
    def __init__(self,limit):
        self.limit = limit
        self.que = []
    def enq(self,data):
        if len(self.que) >= self.limit:
            print("FUll que exception")
        else:
            self.que.append(data)
    def dq(self):
        if len(self.que) == 0:
            print("EMPTY queue exception")
        else:
            print(self.que[0])
            del self.que[0]
    def travel(self):
        if len(self.que) !=0 :
            for i in self.que:
                print("the data is ",i)
        else :
            print("The que is empty")
                
        
# Here in all the previous and the next to come examples we are printng exceptions
# Ideally we should be raising exceptions to prevent the further execution of code
