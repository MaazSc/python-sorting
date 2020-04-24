size=int(input("Enter the size of array: ")) #getting size of list from user
arr=[] #list/array creation
for i in range(0,size): #this loop runs from 0 to size. i.e; 0,1,2,3,4,5 if size value is 6, to get the number of inputs from the user
    inp=int(input("Enter the elements: ")) #getting input from the user
    arr.append(inp) #appending the input values with the list
search=int(input("Enter the element you want to search in an array: ")) #printing the list
if search in arr: # if search element is present in arr
    print("present!") # this will be printed
    print(arr.index(search)) #  and the index where search element is present will also be printed
else: # if search element is not found
    print("Not found") # this will be printed
