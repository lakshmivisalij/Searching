
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
