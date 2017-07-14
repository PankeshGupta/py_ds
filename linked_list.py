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
        return self.next
    def set_next_node(self,next_node):
        self.next_node = next_node
        
if __name__ == "main":
    main()
