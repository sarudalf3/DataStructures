class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList: #create a linked instance
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val): #function to add to front instance
        new_node = SLNode(val)	#use the SLNode class
        current_head = self.head
        new_node.next = current_head
        self.head = new_node #Insert the created list as a header list
        return self	#chained

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next #insert the neighboor runner
        return self	#chained

    def add_to_back(self, val):
        if self.head == None:	#empty list case
            self.add_to_front(val)	# execute add_to_front method
            return self	#Make sure the next lines don't execute

        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next #Go over all neighboors to find the last one
        runner.next = new_node	#Insert the element as the last one of the list
        return self #Chained

    def remove_from_front(self):
        runner = self.head.next
        self.head = runner
        return self

    def remove_from_back(self):
        runner = self.head
        while (runner.next != None): #Go over all neighboors to find the last one
            last_runner = runner
            runner = runner.next
        last_runner.next = None
        return self #Chained

    def remove_val(self, val):
        runner = self.head
        
        if (runner is not None):
            if(runner.value == val):
                self.head = runner.next
                runner = None
                return self

        while (runner is not None):
            if (runner.value == val):
                break
            prev = runner
            runner = runner.next

        if (runner == None):
            return self

        prev.next = runner.next
        runner = None
        return self    

    def insert_at(self, val, n):
        runner = self.head
        idx = 1
        
        if n == 0:
            new_node = SLNode(val)
            new_node.next = self.head
            self.head = new_node
            return self
        
        while idx < n and runner is not None:
            runner = runner.next
            idx = idx+1

        if runner is None:
            print("Index out of bound")
            return self
        else: 
            new_node = SLNode(val)
            new_node.next = runner.next
            runner.next = new_node
        return self   

print("*"*12)
my_list = SList() #New class
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values().remove_from_front().print_values() # encadenamiento, yeah!
print("*"*12)
my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values().remove_from_back().print_values() # encadenamiento, yeah!
print("*"*12)
my_list = SList()	#New class
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.remove_val("are").print_values()
print("*"*12)
my_list = SList()	#New class
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.remove_val("Linked lists").print_values()
print("*"*12)
my_list = SList()	#New class
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.remove_val("fun!").print_values()
print("*"*12)
my_list = SList()	#New class
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.remove_val("fun").print_values()
print("*"*12)
my_list = SList()	#New class
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

my_list.insert_at("The",0).insert_at("worthy",1).insert_at("so",4).insert_at("awesome",6).insert_at("error",8).print_values()
