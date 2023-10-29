
#one issue here. Deleting last node NOT works
class node:
    #Node for double linked list
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
        
        
class doubleLinkedList:
    def __init__(self):
        self.head = None
        
    def addBeginning(self, val):
        newNode = node(val)
        
        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            
    def addEnd(self, val):
        newNode = node(val)
        
        if(self.head == None):
            self.head = newNode
        
        temp = self.head
        
        while(temp.next != None):
            temp = temp.next
            
        temp.next = newNode
        newNode.prev = temp
        
    def print(self):
        temp = self.head
        if(temp == None):
            print("linked list empty")
            
        while(temp):
            print(temp.data)
            temp = temp.next
     
    def search(self, val):
        if (self.head == None):
            print("List empty")
            return 0
        temp = self.head
        while(temp):
            if(temp.data == val):
                print("key found:")
                return 1
            else:
                temp = temp.next
        return 0
        
    def delete(self, val):
        if (self.head == None):
            print("List empty")
            return 0
        if(self.head.data == val):
            self.head = self.head.next;
            self.head.prev = None
            return
        else:
            temp = self.head
            while(temp.next != None):
                if(temp.next.data == val):
                    temp.next = temp.next.next
                    temp.next.prev = temp
                    return
                temp = temp.next
                
            
    
    
dList = doubleLinkedList()

dList.addBeginning(50)
dList.addBeginning(10)
dList.addBeginning(20)
#print data
dList.print()

print("new One")
dList.addEnd(100)
#print data
dList.print()


print("Is the device prsent == {}".format(dList.search(70)))

#delete
dList.delete(20)
print("after deleting 20")
dList.print()


#delete
dList.delete(10)
print("after deleting 100")
dList.print()
