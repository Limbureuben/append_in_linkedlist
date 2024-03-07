class node:
    def __init__ (self, data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__ (self):
        self.head = None
        
        
    def append(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            
    def search(self, key):
        current = self.head
        index = 0
        if current is not None:
            if current.data == key:
                return index
            current = current.next
            index += 1
            return -1
        
    def printlinkedlist(self):
        while self.head is not None:
            print(self.head.data, end = "---->")
            self.head = self.head.next
            print("NULL")
            
linkedlist = linkedlist()

linkedlist.append(5)
linkedlist.append(6)
linkedlist.append(10)
linkedlist.append(4)

search = linkedlist.search(4)

if search != -1:
    print("Element 4 found at index:", search)
else:
    print("Element 4 is not found in the linkedlist")
                
                
            
                    