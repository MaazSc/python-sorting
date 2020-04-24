array1=[] #list/array creation
size=int(input("Enter array size: ")) # getting size of list from user
for i in range(0,size): # this loop runs from 0 to size. i.e; 0,1,2,3,4,5 if size value is 6, to get the number of inputs from the user
    inp=int(input("Enter values: ")) # getting input from the user
    array1.append(inp) # appending the input values with the list
print(array1) # printing the list
def selectionsort(array1,size): # function creation, passing 2 parameters. i.e; list and the size
    for i in range(0,size-1): #  this loop will start from 0 and end at size-1. eg: size is 6, then will run till 5.
        minpos=i # each time min position will be iterated
        for j in range(i+1,size): # unsorted list decreases as i decreases each time, loop runs from i to size
            if array1[j]<array1[minpos]: # at first, index 0th value  is considered as minimum, but when we find array[j]'s value is less, we update minpos
                minpos=j # minpos holds j, which we found as less than minpos
        temp=array1[i] # array1[i] is kept in temp
        array1[i]=array1[minpos] # array1[minpos] is assigned to array1[i]
        array1[minpos]=temp # temp value is now assigned to array1[minpos]
        print(array1) #printing the array in each iteration
selectionsort(array1,size) # function call
print(array1) # printing the sorted array
