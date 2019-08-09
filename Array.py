# import array

# arr = array.array('i',[1,2,3])
#
# print("The new created array is : ",end="")
#
# for i in range(len(arr)):
#     print(arr[i], end=" ")
#
# print('\r')
# arr.append(4)
#
# print('The appended array is : ',end="")
#
# for i in range(len(arr)):
#     print(arr[i], end=" ")
#
# print('\r')
# arr.insert(2,5) # first argument is index number and second argument is value
#
# print('The array after insertion is : ',end="")
#
# for i in range(len(arr)):
#     print(arr[i], end=" ")
#
# print('\r')
# print("The popped element is : ",end="")
# print(arr.pop(3))   #It takes index number as a argument to pop
#
# print("The array after popped is :",end="")
# for i in range(len(arr)):
#     print(arr[i],end=" ")
#
# print('\r')
# arr.remove(5)  #In this 5 is value. which value you want to del. Give in function.
# print("The array after removing is :",end="")
# for i in range(len(arr)):
#     print(arr[i],end=" ")
#
# print('\r')
# print(arr.index(4)) #index() it will give you index number and 4 is a value in array.
#
# arr.reverse()
# print("The array after reversing is : ",end="")
# for i in range(len(arr)):
#     print(arr[i],end=" ")
#
# print('\r')
# print(arr.typecode)
# print(arr.itemsize)
# print(arr.buffer_info()) # first is address where array is stored and second is number of elements

#

# arr1 = array.array('i',[1,2,3,2,1,4,2,4])
#
# arr2 = array.array('i',[1,2,3])
#
# print("The occurrences of 1 in array is : ",end="")
# print(arr1.count(1))
#
# arr1.extend(arr2)
# for i in range(len(arr1)):
#     print(arr1[i],end = " ")
# #
# print('\r')
#
arr = array.array('i',[1,2,3,1,2,5])

li = [1,2,3]

arr.fromlist(li)
print("The modified array is :",end="")
for i in range(len(arr)):
    print(arr[i],end=" ")

print('\r')
print(type(arr))
a = arr.tolist()
print("Array into list: ",a)
print(type(a))










