class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
# print Linked List
        
def printLL(head):
    if head is None:
        return head
        
    while head is not None:
        print(str(head.data) + '->', end = ' ')
        head = head.next
    print('None')    
    return


 # insert  into Linked List
 
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
    
head = takeInputLL()
printLL(head)
