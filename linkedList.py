class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def printLL(head):
    if head is None:
        return head
        
    while head is not None:
        print(str(head.data) + '->', end = ' ')
        head = head.next
    print('None')
    
    return

        
def takeInputLL():
    inputList = [int(ele) for ele in input().split()]
    
    head = None
    tail = None
    
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        
        if head is None:
            head = newNode
            tail = newNode
            
        else:
            tail.next = newNode
            tail = newNode
            
    return head
    
    
    
#insert at a particular position of a linked list - Iteratively

def InsertAtIIter(head, i, data):
    
    if i >= lengthLL(head):
        return head
    
    newNode = Node(data)
  
    if i == 0:
        newNode.next = head
        head = newNode
        
    else:
        prev = None
        curr = head
        count = 0
        while count < i:
            prev = curr
            curr = curr.next
            count += 1
        if i == lengthLL(head)-1:
            curr.next = newNode
            return head
        else:
            prev.next = newNode
            newNode.next = curr
        
    
    return head

# Length of a Linked List 

def lengthLL(head):
    count = 0
    while head is not None:
        count += 1 
        head = head.next
    return count
    
head = takeInputLL()
printLL(head)

head = InsertAtIIter(head, 3, 7)



printLL(head)
