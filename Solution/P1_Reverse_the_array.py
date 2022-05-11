# Reverse the arra

array=list(map(int,input("Enter Element of List in single line with space\n").split()))

# Inbuilt Method

# array.reverse()
# print(array)

# Brute Force and Using Another Array


# rev_arr=[]
# for i in range(len(array)-1,-1,-1):
#     rev_arr.append(array[i])
# print(rev_arr)


#Reversing the array and storing in same array
j=-1
for i in range(len(array)//2):
    array[i],array[j]=array[j],array[i]
    j-=1

print(array)