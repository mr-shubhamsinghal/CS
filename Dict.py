# d = {'first':'String value','second':[1,2]}

# print(d.keys())  #no order, no duplicate keys
# print(d.values())
# print(d['first'])
# print(d.items())
# print(d.get('first')) # get and pop both are same
# print(d.pop('second'))
# print(d.popitem())
#Methods to create a new dictionary

# d1 = {'a':[1,2]}
# d2 = d1
# d1['a'] = [1,2,3,4,5]
# print(d2)

# d1 = {'a':[1,2]}
# d2 = d1.copy()
# d1['a'] = [1,2,3,4,5]
# print(d2)

#or

# d1 = {'a':[1,2]}
# d1.setdefault('third','')
# print(d1)
# print(d1.clear())

# d1 = {'a':1}
# d2 = {'a':2,'b':2}
# d1.update(d2)
# print(d1,d2)


