class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
#first_node = Node(21)
#print(f"first node - {first_node}")
#print(f"first node - {first_node.value}")

class SLL:
    def __init__(self, head = None):
        self.head = head
    
    def front(self):
        if self.head != None:
            print(self.head.value)
            return self.head
        return "null"

    def add_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if self.head == None:
            return "null"
        self.head == new_node
        print(SLL)
        return self

    def remove_front(self):
        if self.head is None:
            print("LL is empty")
        self.head = self.head.next
        return self
        
    #add to back
    def addToBack(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def display(self):
        str_node = ""
        node_num = 1
        runner = self.head
        while runner: #same as while runner != None

            str_node += f"the value of {node_num} node is {runner.value}"
            node_num += 1
            runner = runner.next
        print(str_node)
        return self

first_sll = SLL(Node(21))
first_sll.addToBack(51).addToBack(71).addToBack(7).addToBack(45)
#print(first_sll.head.next.value)




first_sll.display()


