# Move all the negative elements to one side of the array 

array=list(map(int,input("Enter Element of Array in Single Line With Space in it:\n").split()))

#Inbuilt Method 
#Same Can be Done by Sorting Algorithm.
# array.sort()
# print(array)

#We can Also do the Same thing with any sorting Algorithm.
#If Negative Numbers are Needed on right Side, reverse function can be applied to it.


for i in range(len(array)):
    if array[i]<0:
        array.append(array[i])
        array.remove(array[i])

print(array)