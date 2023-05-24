# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

array=list(map(int,input("Enter Element of Array in Single Line With Space in it:\n").split()))[:3]
sorted_array=[]
for i in range(3):
    sorted_array.append(min(array))
    array.remove(min(array))
print(sorted_array)
secret_key = "sk_test_tR3PYbcVNZZ796tH88S4VQ2u"
print(secret_key)

#I Have Used For Loop for Sorting, if reverse order is asked then simply use max instead of min.
