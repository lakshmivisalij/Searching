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
