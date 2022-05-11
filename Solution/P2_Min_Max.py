#Find the maximum and minimum element in an array


array=list(map(int,input("Enter Element of Array in Single Line With Space in it:\n").split()))

#Inbuilt Method

# print("Maximum Element in List is:",max(array))
# print("Minimum Element in List is:",min(array))

#Brute Force Method

minimum=array[0]
maximum=array[0]

for i in range(len(array)):
    if array[i]<=minimum:
        minimum=array[i]
    
    if array[i]>=maximum:
        maximum=array[i]

print("Maximum Element in List is:",maximum)
print("Minimum Element in List is:",minimum)