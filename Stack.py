#Pushing and Poping from a stack. Using a Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def __str__(self):
        return str(self.top.next.data)
    
    def push(self,data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top == None:
            return None
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp
        
SS = Stack()
SS.push("Omar")
SS.push("Younes")
SS.push("Amine")
print(SS)

print(SS.pop())