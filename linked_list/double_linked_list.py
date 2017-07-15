class double_link_list():
    def __init__(self,data):
        node_initialized = Node(data)
        self.head = node_initialized
        self.length = 1
        self.bin = []
        print("double link list initialized ")
    #=== get a node at a specific position =========
    def get_node(self,pos):
        fetch_pos = pos
        i = 1
        current_node = self.head
    
        if fetch_pos <= self.length and fetch_pos>=0:
                while i < fetch_pos :
                    current_node = current_node.get_next_node()
                    i+=1
                return current_node
                    
        else:
            print("invalid position")
                    
                        
    #==== getter and setter method for head ========
    def get_head(self):
        return self.head
    def set_head(self,new_head):
        self.head = new_head
    #========== adding nodes =======================
    def add_node_last(self,data):
        new_node = Node(data)
        last_node  = self.get_node(self.length)
        
        last_node.set_next_node(new_node)
        new_node.set_previous_node(last_node)
        self.length +=1
        print("node added sucessfully")
    def add_node_begin(self,data):
        new_node = Node(data)
        first_node = self.head
        new_node.set_next_node(first_node)
        first_node.set_previous_node(new_node)
        self.set_head(new_node)
        self.length+=1
        print("new node added succesfully")
    def add_node(self,data,pos):
        if pos == 1:
            self.add_node_first(data)
        elif pos == self.length :
            self.add_node_end(data)
        elif pos in range(2,self.length):
            new_node = Node(data)
            previous_node = self.get_node(pos)
            # front connections for new node
            new_node.set_next_node(previous_node.get_next_node())
            previous_node.get_next_node().set_previous_node(new_node)
            # backward connections
            new_node.set_previous_node(previous_node)
            previous_node.set_next_node(new_node)
            self.length +=1
            print("node added succesfully")
        else:
            print("invalid position please enter correct position no.")
    #==== deleting nodes ==============
    def delete_last_node(self):
        last_node = self.get_node(self.length)
        last_node.get_previous_node().set_next_node(None)
        self.bin.append(last_node)
        del last_node
        self.length -=1
        print("The node has been sucesfully deleted")
        print("=====================================")
        print(" to get back deleted elements use retrieve elements")
    def delete_first_node(self):
        first_node = self.get_head()
        first_node.get_next_node().set_previous_node(None)
        self.set_head(first_node.get_next_node())
        self.length -= 1
        self.bin.append(first_node)
        print("The node has been sucesfully deleted")
        print("=====================================")
        print(" to get back deleted elements use retrieve elements")
    def delete_node(self,pos):
        if pos==1:
            self.delete_first_node
        elif pos==self.length:
            self.delete_last_node
        elif pos in range(2,self.length):
            a_node = self.get_node(pos)
            a_node.get_previous_node().set_next_node(a_node.get_next_node())
            a_node.get_next_node().set_next_node(a_node.get_previous_node())
            self.length -=1
            print("The node has been sucesfully deleted")
            print("=====================================")
            print(" to get back deleted elements use retrieve elements")
            
        

            
    #==== travelling nodes ==============
    def travel_f(self):
        current_node = self.get_head()
        while current_node != None :
            print("The node is ",current_node.get_data())
            current_node = current_node.get_next_node()
    def travel_r(self):
        i = self.length
        last_node = self.get_node(i)
        while i>=1:
            print("--R---: The data is :", last_node.get_data())
            i = i-1
            last_node = last_node.get_previous_node()

    #===== retreving deleted elements =========
    def get_back(self):
        last_deleted = self.bin.pop()
        print(last_deleted)
        self.add_node_last(last_deleted.get_data())
        self.length+=1
        print("elemnet added back")


#================= class node starts ========================        
class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None
        self.previous_node = None
    def get_next_node(self):
        return self.next_node
    def get_previous_node(self):
        return self.previous_node
    def get_data(self):
        return self.data
    def set_next_node(self,next_node):
        self.next_node = next_node
    def set_previous_node(self,previous_node):
        self.previous_node = previous_node
    def set_data(self):
        self.data = data
