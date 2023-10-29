#deleting is missing here
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
        
    def addFirst(self, key):
        newNode = node(key)
        if(self.head == None):
            self.head = newNode
            newNode.next = newNode
        else:
            last = self.head
            while(last.next != self.head): #This is not None and root node
                last = last.next
            last.next = newNode
            newNode.next = self.head
            self.head = newNode
        
    def addLast(self, key):
        newNode = node(key)
        if(self.head == None):
            newNode.next = newNode
            self.head = newNode
        else:
            last = self.head
            while(last.next != self.head):
                last = last.next
            last.next = newNode
            newNode.next = self.head
    
    def printList(self):
        temp = self.head
        if(temp == None):
            print("Empty")
        while True:
            print(temp.data)
            temp = temp.next
            if(temp == self.head):
                break
    
    def search(self, key):
        if(self.head == None):
            print("llist empty")
            return
        
        temp = self.head
        while True:
            if(temp.data == key):
                print("match found")
                return 1
            else:
                temp = temp.next
            if(temp == self.head):
                return 0
        return 0
        
    def delete(self, key):

        if self.head == None:
            return
        
    

llist = CircularLinkedList()
print("Inserting Element: 10")
llist.addFirst(10)
print("Inserting Element: 20")
llist.addFirst(20)
print("Inserting Element: 30")
llist.addFirst(30)
print("Circular Linked List Elements Are:")
llist.printList()
print("Inserting Element: 10")
llist.addLast(10)

print("Inserting Element: 20")
llist.addLast(20)

print("Inserting Element: 30")
llist.addLast(30)

print("Circular Linked List Elements Are:")
llist.printList()   

print("Is value in linkedlist = {}".format(llist.search(20)))

print("Deleting Element: ",30)
llist.delete(30)

print("The LinkedList Elements Are [After Deletion]:")
llist.printList()
        
        
        
        
