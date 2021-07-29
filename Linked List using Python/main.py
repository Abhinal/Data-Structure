class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
#To Display Data
    def display(self):
        print("Data:", end=" ")
        pointer = self.head
        while pointer is not None:
            print(pointer.data, end= ' ')
            pointer = pointer.next
        print()
#To Create Linked List
    def create(self, num=0):
        self.head = Node(input("Enter: "))
        pointer = self.head
        while num-1>0:
            pointer.next=Node(input("Enter: "))
            pointer=pointer.next
            num-=1
#To Count the Number of Data
    def count(self):
        pointer = self.head
        count = 0
        while(pointer is not None):
            count +=1
            pointer = pointer.next
        return count
#To Add at Begin
    def AtBegin(self, newData):
        temp = Node(newData)
        temp.next = self.head
        self.head = temp
#To Add at Last
    def AtEnd(self, newData):
        temp = Node(newData)
        pointer = self.head
        if pointer is None:
            self.head = temp
            return
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = temp
#To Add in Between
    def InBetween(self, index, data):

        if index<=self.count() and index>=0:
            midNode = self.head
            temp=Node(data)
            if index==0:
                temp.next = self.head
                self.head = temp
                return
            while(index>1):
                midNode = midNode.next
                index-=1
            temp.next = midNode.next
            midNode.next = temp
#To Remove Node
    def RemoveNode(self, key):
        if self.head==None:
            return
        
        pointer = self.head
        if(pointer.data == key):
            self.head = pointer.next
            pointer = None
            return

        while(pointer is not None):
            if pointer.data == key:
                break
            previous = pointer
            pointer = pointer.next

        if pointer==None:
            return
        
        previous.next=pointer.next
        pointer=None

#To Print Menu
def printMenu():
    print("Enter 1 for Display Data: ")    
    print("Enter 2 for data input At Begin: ")    
    print("Enter 3 for data input At End: ")    
    print("Enter 4 for data input In Between: ")    
    print("Enter 5 for Remove Data: ")    
    print("Enter 6 for Length: ")    
    print("Enter 9 for Menu")  
    print("Enter 0 for Exit: ")


#Driver Code
if __name__=="__main__":
    list1 = SingleLinkedList()
    num =int(input("Enter Number of Data to Create Linked List: "))
    list1.create(num)

    printMenu()
    while(True):
        choice = int(input("\nEnter your choice: "))
        
        if choice==1:
            list1.display()
        elif choice==2:
            list1.AtBegin(input("Enter Data: "))
        elif choice==3:
            list1.AtEnd(input("Enter Data: "))
        elif choice==4:
            list1.InBetween(int(input("Enter Index: ")), input("Enter Data: "))
        elif choice==5:
            list1.RemoveNode(input("Enter Key: "))
        elif choice==6:
            print("Total Count:", list1.count())
        elif choice==0:
            exit('Good Bye')
        else:
            printMenu()




