# Find the Union and Intersection of the two sorted arrays.

def union(array1,array2):
    array1.extend(array2)
    array3=set(array1)
    array3=list(array3)
    return array3

def intersection(array1,array2):
    array4=[]
    if len(array1)<len(array2):
        for i in array1:
            if i in array2:
                array4.append(i)

    else:
        for i in array2:
            if i in array1:
                array4.append(i)

    return array4


array1=list(map(int,input("Enter Element of Sorted Array in Single Line With Space in it:\n").split()))
array2=list(map(int,input("Enter Element of Sorted Array in Single Line With Space in it:\n").split()))

#Intersection means the element lies in both arrays
print("The Intersection of both array is:",intersection(array1,array2))

#union means all element in both array
print("The Union of both array is:",union(array1,array2))