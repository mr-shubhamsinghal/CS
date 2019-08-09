# quick example

# l = [1,2,3]
# print(l[0])
# l.append(5)
# print(l)

# Diff b/w append() and extend()

# stack = ['a','b','c']
# stack.append(['a','d','f'])
# print(stack)
#
# stack = ['a','b','c']
# stack.extend(['a','d','f'])
# print(stack)

#other list methods
#index
# my_list = ['a','b','c','d','b','f']
# print(my_list.index('b'))
# print(my_list.index('b',2,3)) #b is a search string in a list, 2 is start index number and 3 is a stop index number for search.

#insert
# my_list = ['a','b','c','d','b','f']
# my_list.insert(2,'a')
# print(my_list)

#remove
# my_list = ['a','b','c','d','b','f']
# my_list.remove('a')
# print(my_list)

#pop
# my_list = ['a','b','c','d','b','f']
# my_list.pop()
# print(my_list)

#count
# my_list = ['a','b','c','d','b','f']
# print(my_list.count('a'))

#sort
# my_list = ['a','b','c','d','b','f']
# my_list.sort()
# print(my_list)
#
# my_list.sort(reverse=True)
# print(my_list)

#reverse
# my_list = ['a','b','c','d','b','f']
# my_list.reverse()
# print(my_list)

#operators
# my_list = [1]
# my_list += [2]
# print(my_list)
# my_list += [3,4]
# print(my_list)

#slicing list[first index:last index:step]
#list[:]
# a = [0,1,2,3,4,5]
# print(a[2:])
# print(a[:2])
# print(a[2:-1])
#
# print(a[:])
# print(a[::1])
# print(a[0::1])

#list comprehension
# a = [i for i in range(10) if i%2==0]
# print(a)

#Filtering Lists
# li = [1,2]
# a = [elem*2 for elem in li if elem>1]
# print(a)

#List as stacks
#used LIFO (last in first out) use append for insert (it is last in) and use pop for remove(it is first out)

#List as queues
#used FIFO (first in first out)
queue = ['a','b','c','d']
# queue.append('e')
# print(queue)
# queue.append('f')
# print(queue)
# queue.pop(0)
# print(queue)

#How to copy a list
#There are three ways to copy a list
l = [1,2,3]    #it is also shallow copy
# print(id(l))
# print(l)
# l2 = list(l)
# print(id(l2))
# print(l2)

# import copy
# l2 = copy.copy(l)
# print(l2)
# print(id(l2))

#shallow copy : it means changes will be reflected in both list when you change in one list
# a = [1,2,[3,4]]
# b = a
# a[2][0] = 10
# print(a)
# print(b)

#deep copy : it means changes will be reflected in one list.
# a = [1,2,[3,4]]
# b = copy.deepcopy(a)
# a[2][0] = 10
# print(a)
# print(b)

#Inserting item into sorted list
# x = [3,1,6,7]
# x.sort()
# import bisect
# # bisect.insort(x,2)
# print(x)
# print(bisect.bisect(x,5)) #purpose of bisect algorithm is to find a position in list where an element needs to be inserted to keep the list sorted.

