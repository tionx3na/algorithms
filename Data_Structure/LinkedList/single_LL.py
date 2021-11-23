# Single linked list operations


# initializing node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# initializing linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the end of the Linked List
    def insert(self,item):
        if self.head == None:
            print("inside head")
            self.head = Node(item)
            self.head.next = None
        else:
            print("not head")
            ptr = self.head
            while(ptr.next != None):
                ptr = ptr.next
            ptr.next = Node(item)

    # Linked List Traversal
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# Execution starts from main
if __name__ == '__main__':

    llist = LinkedList()

    llist.printList()

    sel = 'y'
    while(sel != "q"):
        ele = int(input("Enter the element to be added"))

        llist.insert(ele)
        llist.printList()

        sel = input("Press y to continue and q to quit")
