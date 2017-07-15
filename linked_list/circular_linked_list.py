#***********  Node adt *******************************

class node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node
    # getter and setter for data
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data = data
    # gettter and setter for next_node

    def get_next_node(self):
        return self.next_node
    def set_next_node(self,next_node):
        self.next_node = next_node
    
#*********** circular linked list adt *********************
class circular_linked_list:
    # init method for double link list
    
    def __init__(self,data):
        init_node = node(data)
        self.head = init_node
        self.length = 1
        self.end_node = self.head
        init_node.set_next_node(self.head)
    # getter setter for self attri
    def get_head(self):
        return self.head
    def set_head(self,new_head):
        self.head = new_head
    def get_end_node(self):
        return self.end_node
    def set_end_node(self,end_node):
        self.end_node = end_node
    
    # adding nodes to the list =========
    
    def add_node_last(self,data):
        init_node = node(data,self.head)
        # creating connections for ending nodes at the end
        self.get_end_node().set_next_node(init_node)
        init_node.set_next_node(self.head)
        # setting the self.end for further reference
        self.set_end_node(init_node)
        # inc. the length after addition of the new node
        self.length+=1
    def add_node_begin(self,data):

        # init a new node
        init_node = node(data)
        
        # make the new node point to the current_head
        init_node.set_next_node(self.head)
        
        #======= a roadblock ==================
        # make change in the head only is a way
        #======================================

        # other way is make change in the head and make the new head point to new head
        # ===== i badly miss pointer here ============================================
        # we have to use copy.shallow copy here
        self.set_head(init_node)
        self.get_end().set_next_node(self.get_head())
        print("noded added at the begin successfully")

    def travel_f(self):
        current_node = self.head
        while current_node.get_next_node()!= self.get_head():
            print("the node data is ----- : ",current_node.get_data())
            current_node = current_node.get_next_node()

            


            













        
        
