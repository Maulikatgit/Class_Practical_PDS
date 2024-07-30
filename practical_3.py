import array

# Given string
given_string = "Hello, World!"

# Positive index slicing
positive_slice = given_string[1:5]
print("Positive index slicing:", positive_slice)
print()

# Negative index slicing
negative_slice = given_string[-6:-1]
print("Negative index slicing:", negative_slice)
print()

# End index > string length slicing
end_slice = given_string[:20]
print("End index > string length slicing:", end_slice)
print()

# Entire string slicing
entire_slice = given_string[:]
print("Entire string:", entire_slice)
print()

chunks = [given_string[i:i + 3]
          for i in range(0, len(given_string), 3)]
print("Chunks of length 3:", chunks)
print()

split_by_comma = given_string.split(',')
print("Split by comma:", split_by_comma)
print()

words = given_string.split()
print("Words in the string:")
for word in words:
    print(word)
print()

# Apply trim (strip)
trimmed_string = given_string.strip()
print("Trimmed string:", trimmed_string)
print()

# Toupper (upper)
uppercased_string = given_string.upper()
print("Uppercased string:", uppercased_string)
print()

#  Tolower (lower)
lowercased_string = given_string.lower()
print("Lowercased string:", lowercased_string)
print()

# Replace string and character
replaced_string = given_string.replace("World", "Universe")
print("Replaced string:", replaced_string)
print()

# Title
titlecased_string = given_string.title()
print("Titlecased string:", titlecased_string)
print()

# Join operation
words = ['Hello', 'World']
joined_string = ' '.join(words)
print("Joined string:", joined_string)
print()

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Operations
set1.add(6)
print("Add element to set1:", set1)
print()

union_result = set1.union(set2)
print("Union of set1 and set2:", union_result)
print()

intersection_result = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_result)
print()

difference_result = set1.difference(set2)
print("Difference of set1 and set2:", difference_result)
print()

symmetric_difference_result = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_result)
print()

set1.intersection_update(set2)
print("Intersection update of set1 with set2:", set1)
print()

set1.symmetric_difference_update(set2)
print("Symmetric difference update of set1 with set2:", set1)
print()

set1.difference_update(set2)
print("Difference update of set1 with set2:", set1)
print()

set1.discard(6)
print("Set1 after discarding element 6:", set1)
print()

issubset_result = set1.issubset(set2)
print("Is set1 a subset of set2?", issubset_result)
print()

issuperset_result = set1.issuperset(set2)
print("Is set1 a superset of set2?", issuperset_result)
print()

isdisjoint_result = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?", isdisjoint_result)
print()

set1.remove(4)
print("Set1 after removing element 4:", set1)
print()

popped_element = set1.pop()
print("Popped element from set1:", popped_element)
print()

set1.clear()
print("Cleared set1:", set1)
print()


# Initialize an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Example operations
arr.append(6)
print("Appended 6 to array:", arr)
print()

arr.extend([7, 8, 9])
print("Extended array:", arr)
print()

arr.insert(3, 10)
print("Inserted 10 at index 3:", arr)
print()

arr.remove(5)
print("Removed element 5:", arr)
print()

index_of_4 = arr.index(4)
print("Index of element 4:", index_of_4)
print()

arr.reverse()
print("Reversed array:", arr)
print()

arr.pop()
print("Popped element from array:", arr)
print()

arr.clear()
print("Cleared array:", arr)
