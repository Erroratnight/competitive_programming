#Find the "Kth" max and min element of an array 

def merge_sort(array,start,end):
    if start<end:
        mid=(start+end)//2
        merge_sort(array,start,mid)
        merge_sort(array,mid+1,end)
        merge(array,start,mid,end)

def merge(array,start,mid,end):
    len_left_array=mid-start+1
    len_right_array=end-mid
    left_array=[0]*(len_left_array)
    right_array=[0]*(len_right_array)
    
    for i in range(len_left_array):
        left_array[i]=array[start+i]

    for j in range(len_right_array):
        right_array[j]=array[mid+1+j]

    left_array.append(100000000)
    right_array.append(100000000)
    i=0
    j=0
    for k in range(start,end+1):
        if left_array[i]<=right_array[j]:
            array[k]=left_array[i]
            i+=1
        else:
            array[k]=right_array[j]
            j+=1


#Driver Code

array=list(map(int,input("Enter Element of Array in Single Line With Space in it:\n").split()))
k=int(input("Enter Which Max and Min Element to be Found Out:"))

#Inbuilt Method

# array.sort()
# print("Maximum Element in List is:",array[-k])
# print("Minimum Element in List is:",array[k-1])

#Sorting With the Help of Merge Sort 
#You Can Use Any Sorting Algorithm 

merge_sort(array,0,len(array)-1)
print("Maximum Element in List is:",array[-k])
print("Minimum Element in List is:",array[k-1])