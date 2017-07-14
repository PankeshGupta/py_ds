class linked_list:
    def __init__(self,head):
        self.head = head
        print("A link list sucessfull created")
    def set_head(self,head):
        self.head = head
    def get_head(self):
        return self.head
    def get_end(self):
        current = self.get_head()
        while current.next_node != None:
            current = current.next_node
        return current
    def travel(self):
        current = self.head
        while current != None:
            print("the data is ",current.data)
            current = current.next_node
    def length(self):
        current = self.get_head()
        length = 0
        while current.get_next_node() != None:
            length+=1
            current = current.get_next_node()
        return length
    def return_node(self,pos):  
        current = self.get_head()
        node_demand = None
        current_pos = 0
        while pos >=0 and pos <= self.length() and current_pos != pos:
            node_demand = current.get_next_node()
            current_pos +=1
        return node_demand
    # insertion method's ##########################        
    def insetion_node_begin(self,data):
        a_node = node(data)
        a_node.next_node = self.get_head()
        self.head = a_node
        print("inseted a new node at the begin")

    def insertion_node_end(self,data):
        a_node = node(data)
        last_node = self.get_end()
        last_node.next_node = a_node
        print("inseted a new node at the end") 
    def insertion_node_pos(self,pos,data):
        postion = None
        if pos==0 :
            self.insertion_node_begin(data)
        elif pos == self.length():
            self.insertion_node_end(data)
        else :
            if pos>0 and pos<self.length():
                a_node = node(data)
                m_node = self.return_node(pos)
                a_node.set_next_node(m_node.get_next_node())
                m_node.set_next_node(a_node)

    # deletion method
    def delete_node(self,pos):
        if pos==0:
            delete_node_begin(pos)
        elif pos == self.length():
            delete_node_end(pos)
        elif pos>0 and pos< self.length():
            previous_node = self.return_node(pos-1)
            current_node = previous_node.get_next_node()
            previous_node.set_next_node(current_node.get_next_node())
            del current_node
            print("node sucessfully deleted")
        
    
    def delete_node_end(self):
        previous_node = self.return_node(self.length()-1)
        last_node = previous_node.get_next_node()
        previous_node.set_next_node(None)
        del last_node
        print("last node succesfully deleted")
    
    def delete_node_begin(self):
        head_node = self.get_head()
        self.set_head(head_node.get_next_node)
        del head_node
        print("Head node succesfully deleted")
    
                
class node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node
        print("a ndoe sucessfully created")
    def set_data(self,data):
        self.set_data = data
        print("data of node changed successfully")
    def get_data(self):
        return self.data
    def get_next_node(self):
        return self.next_node
    def set_next_node(self,next_node):
        self.next_node = next_node
        
if __name__ == "main":
    main()
