#constructing tuples

# l=(1,23,3)
# print(l[0])
# l = 1,2,4,5,5,2
# print(l)
# print(type(l))
# print((1,)*4)
# s = (1,0)
# s += (4,)
# print(s)

#Tuple methods

# l = (1,2,4,4)
# print(l.count(4))
# print(l.index(2))

#Interests of Tuple
#Tuple as key pairs to build dictionaries
# d = dict([('jan',1),('feb',2),('march',3)])
# print(d['feb'])

#signing multiple values
# (x,y,z) = ('a','b','c')
# print(x)
# (x,y,z) = range(3)
# print(y)

#Tuple unpacking
# data = (1,2,3)
# x,y,z = data
# print(y)

#Swap
# x = 2
# y = 4
# (x,y)=(y,x)
# print(x, y)

#Misc
#length
# t = (1,2)
# print(len(t))
#Slicing
# t = (1,2,3,4,5)
# print(t[2:])
#copy a tuple
# t = (1,2,3,4,5)
# newt = t
# print(newt)

#tuple are not fully immutable : if a value in a tuple is mutable, then you can change it
# t = (1,2,[3,5])
# print(t)
# t[2][0] = 4
# print(t)
#convert a tuple to a string
# print(str(t))

#math and comparison
# t = (1,2,3)
# print(max(t))
