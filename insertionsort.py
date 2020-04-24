def Insertion(arr):  # function creation
    for i in range(1,size):  # arr[0] is considered as sorted sublist,this loop runs from 1 to size-1 of an array, why this loop starts at 1 is: 0th position of array is considered as sorted
        temp=arr[i] # for the above loop, i at first iteration is
        j=i-1 # j will be immediate left of i,eg: if i is arr[2] then j will be arr[1]
        while j >= 0 and arr[j] > temp:  # why j > or = 0 is, if i is 0th position, then j=-1, j=-1 means, there are no values on the left of i, and arr[j]>temp
            arr[j+1]=arr[j]  # then arr[j] is assigned as arr[j+1], to the next place and arr[j] is made empty
            j -= 1 # j=j-1, comparing the second left,then third left and so on
        arr[j+1] = temp  # temp value is stored in arr[j+1]
temp=0  #temp is assigned as 0
size=int(input("Enter array sze: "))  # getting the input size
arr=[]  # array/list creation
for i in range(0,size):  # this loop runs from 0 to size
    inp=int(input())  # getting input
    arr.append(inp)  # appending the values to array
Insertion(arr)  # function call
print(arr)  # printing the array


