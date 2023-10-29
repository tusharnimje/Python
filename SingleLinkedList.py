#Linked list

#This is node strcuture
class node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Class linked list which holds the head node of a linked list

class linkedList():
    def __init__(self):
        self.head = None
        
    def printNode(self):
        temp = self.head
        while(temp):
            print("{} ".format(temp.data))
            temp = temp.next
            
    def insertBeginnig(self, val):
        tempNode = node(val)
        tempNode.next = self.head
        self.head = tempNode
        
        
    def insertLast(self, val):
        tempNode = node(val)
        last = self.head
        
        while(last.next):
            last = last.next
        last.next = tempNode
        
    def find(self, val):
        if (self.head == None):
            return 0;
        temp = self.head
            
        while(temp):
            if(temp.data == val):
                return 1
            temp = temp.next
        return 0
        
    def delete(self, val):
        if(self.head == None):
            print("list is empty")
            return
        
        if(self.head.data == val):
            print("key found")
            self.head = self.head.next
            
        temp = self.head
        while(temp.next):
            if(temp.next.data == val):
                print("node found to delete")
                temp.next = temp.next.next
                break
            else:
                temp = temp.next
        

        
llist = linkedList()

node1 = node(10)
node2 = node(20)
node3 = node(30)

llist.head = node1
node1.next = node2
node2.next = node3

print("Normal list")
llist.printNode()
#Insett node at the beginning
llist.insertBeginnig(50)
print("insert beginning list")
llist.printNode()

#Insert at the end of a linked list
llist.insertLast(70)
print("insert last list")
llist.printNode()

print("searching for a list")
print("is it found == {}".format(llist.find(45)))


print("deleting a key from linked list")
llist.delete(70)
print("llist after deleting 70")
llist.printNode()




