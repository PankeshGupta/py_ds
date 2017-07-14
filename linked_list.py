class linked_list:
    def __init__(self,head = None):
        self.head = head
        print("A link list sucessfull created")
    def set_head(self,head):
        self.head = head
    def get_head(self):
        return self.head

class node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node

    def set_data(self,data):
        self.set_data = data
        print("data of node changed successfully")
    def get_data(self):
        return sel.data
    def get_next(self):
        return self.next
    def set_next_node(self,next_node):
        self.next_node = next_node
        
if __name__ == "main":
    main()
