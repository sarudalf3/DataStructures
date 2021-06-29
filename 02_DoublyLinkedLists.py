class DLNode:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

class DList: #create a linked instance
    def __init__(self):
        self.head = None

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next #insert the neighboor runner
        return self	#chained
    
    def insert_at_start(self, val):
        if self.head is None: #case when list is null
            new_node = DLNode(val)
            self.head = new_node
            return self

        new_node = DLNode(val)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return self

    def insert_at_end(self, val):
        if (self.head is None): #case when list is null
            new_node = DLNode(val)
            self.head = new_node
            return self
        
        runner = self.head

        while runner.next is not None:
            runner = runner.next

        new_node = DLNode(val)
        runner.next = new_node
        new_node.prev = runner
        return self    

    def insert_before_at(self, prev_node, val): #insert after prev_node
        if self.head is None:
            print("List is empty")
            return self
        else:
            runner = self.head
            while runner is not None:
                if(runner.value == prev_node):
                    break
                runner = runner.next

            if runner is None:
                print("item not in the list")
                return self
            else:
                new_node = DLNode(val)
                new_node.next = runner
                new_node.prev = runner.prev
                
                if runner.prev is not None:
                    runner.prev.next = new_node
                
                runner.prev = new_node
            return self

    def insert_after_at(self, prev_node, val): #insert after prev_node
        if self.head is None:
            print("List is empty")
            return self
        else:
            runner = self.head
            while runner is not None:
                if(runner.value == prev_node):
                    break
                runner = runner.next

            if runner is None:
                print("item not in the list")
                return self
            else:
                new_node = DLNode(val)
                new_node.prev = runner
                new_node.next = runner.next
                
                if runner.next is not None:
                    runner.next.prev = new_node
                
                runner.next = new_node
            return self

    def remove_value(self, val):
        if self.head is None: #Empty list
            print("The list has no element to delete")
            return self

        if self.head.next is None: #One element is head
            if self.head.value == val: #element to delete is on head
                self.head = None
            else:
                print("Item not found")
            return self

        if self.head.value == val: #The element to remove is head
            self.head = self.head.next
            self.head.prev = None
            return self
        
        #Other cases
        runner = self.head
        while runner.next is not None:
            if runner.value == val:
                break;
            runner = runner.next

        if runner.next is not None:
            runner.prev.next = runner.next
            runner.next.prev = runner.prev
            return self
        else:
            if runner.value == val:
                runner.prev.next = None
                return self
            else:
                print("Element not found")
                return self


my_list = DList()	#New class
my_list.insert_at_end("are").insert_at_start("Linked lists").insert_at_end("fun!").print_values()
my_list.insert_before_at("fun!", "so").insert_after_at("fun!", "Awesome").remove_value("fun!").print_values()
