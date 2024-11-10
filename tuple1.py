my_tuple=(1,2,3,4,5)
print(my_tuple)

#accessing tuple
print(my_tuple[0])
print(my_tuple[3])

#slicing tuple
print(my_tuple[1:4])

#concatenating tuples
another_tuple=(6,7,8)
combined_tuple=my_tuple+another_tuple
print(combined_tuple)

#repeating tuple
repeated_tuple=my_tuple*2
print(repeated_tuple)

#length
print(len(my_tuple))

#iterating
for item in my_tuple:
    print(my_tuple)

#methods
print(my_tuple.count(2))
print(my_tuple.index(4))

#deleting tuple
del my_tuple
