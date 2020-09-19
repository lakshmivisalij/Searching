
# Linear Search Arrays Iteration

t = int(input("Enter number of test cases: "))
while t > 0:
	n = int(input("Enter number of elements in an array: "))
	print("Enter elements of the array: ")
	arr=list(int(i) for i in input().strip().split(' '))
	k = int(input("Key to search: "))
	f=0
	for i in range(0,n):
		if k == arr[i]:
		    f = 1
		    print(i)
		    break
	if f==0:
	    print(-1)
	t-=1
	
	
	
# Linear Search Arrays Recursion

def linearSearchRec(arr, key, i):
    if len(arr)==0:
        return -1
    
    if arr[0]==key:
        return i
    return linearSearchRec(arr[1:], key, i+1)
    
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]    
index = linearSearchRec(arr, 5, 0)
print(index)


## Linear Search Linked List - Iteration and Recursion

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

newNode1 = Node(15)
newNode2 = Node(13)
newNode3 = Node(12)
newNode4 = Node(5)
newNode5 = Node(8)
newNode6 = Node(1)


newNode1.next = newNode2
newNode2.next = newNode3
newNode3.next = newNode4
newNode4.next = newNode5
newNode5.next = newNode6

def prinLL(head):
    while head is not None:
        print(str(head.data) + '->', end = ' ')
        head = head.next
    print('None')    
 
	
# Linear Search Linked List Iteration

def linearSearchLLIter(head, key):
    i = 0
    while head is not None:
        if head.data == key:
            return i
        head = head.next
        i += 1
    return -1

# Linear Search Linked List Recursion

def linearSearchLLRec(head, key, i):
    if head is None:
        return -1
        
    if head.data==key:
        return i
        
    return linearSearchLLRec(head.next, key, i+1)
    
    
        
prinLL(newNode1)
ind = linearSearchLLIter(newNode1, 1)
indRec = linearSearchLLRec(newNode1, 1, 0)
print("index: ", ind)
print("index: ", indRec)
