# Tuples are immutable data types eaning once they are created,
# their elements cannot be changed. Here are some key characteristics and operations of tuples in Python:

# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

# Creating a tuple without parentheses (comma-separated values)
another_tuple = 4, 5, 6
print(another_tuple)  # Output: (4, 5, 6)

# Creating a tuple with a single element (comma is needed)
single_element_tuple = (7,)
print(single_element_tuple)  # Output: (7,)

# Empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()


# Accessing Tuple Elements

# Accessing elements
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
print(my_tuple[-1]) # Output: 5 (last element)


# Tuple Operations

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated = tuple1 + tuple2
print(concatenated)  # Output: (1, 2, 3, 4)

# Repetition
repeated = tuple1 * 3
print(repeated)  # Output: (1, 2, 1, 2, 1, 2)

# Slicing

# Slicing
my_tuple = (0, 1, 2, 3, 4, 5)
sliced = my_tuple[1:4]
print(sliced)  # Output: (1, 2, 3)

# Tuple Built-in methods
# count(x): Returns the number of times x appears in the tuple.
# index(x): Returns the index of the first occurrence of x in the tuple. 
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))  # Output: 3
print(my_tuple.index(3))  # Output: 2


# Unpacking of tuple 

# Unpacking
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Using * to capture remaining elements
my_tuple = (1, 2, 3, 4, 5)
a, *b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5


# Immutable tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This would raise a TypeError

# Tuple containing a mutable object
nested_tuple = (1, [2, 3], 4)
nested_tuple[1][0] = 99
print(nested_tuple)  # Output: (1, [99, 3], 4)


# Tuple as a key in a dictionary
my_dict = {(1, 2): "value1", (3, 4): "value2"}
print(my_dict[(1, 2)])  # Output: value1




