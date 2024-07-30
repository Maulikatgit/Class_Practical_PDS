# step 1: Create a list named “Subjects” by inserting 10 subjects into it through any loop
Subjects = []
for i in range(1, 11):
    Subjects.append(f"Subject {i}")
print("Subjects list:", Subjects)
print()

# Step 2: create a list “Elective Subjects” with 5 subjects through direct initialization.
Elective_Subjects = ["Elective 1", "Elective 2", "Elective 3", "Elective 4", "Elective 5"]
print("Elective Subjects list:", Elective_Subjects)
print()

# Step 3: Extend list “Subject” by another list “Elective Subjects”.
Subjects.extend(Elective_Subjects)
print("Extended Subjects list:", Subjects)
print()

# Step 4: Append 3 duplicate subjects into “Subject” list.
Subjects.append("Subject 1")
Subjects.append("Subject 3")
Subjects.append("Subject 7")
print("Subjects list with duplicates:", Subjects)
print()

# Step 5: Find the index of first occurrence of that duplicate value
duplicate_value = "Subject 1"
index = Subjects.index(duplicate_value)
print(f"Index of first occurrence of '{duplicate_value}':", index)
print()

# Step 6: then remove all the occurrences of that specific subject through loop.
while duplicate_value in Subjects:
    Subjects.remove(duplicate_value)
print("Subjects list after removing all duplicates of 'Subject 1':", Subjects)
print()


# Step 7: Define function remove range(i1,i2) to remove range of element from i1 to i2 through del keyword and return the resultant list.
def remove_range(lst, i1, i2):
    del lst[i1:i2]
    return lst


# Example usage:
Subjects = remove_range(Subjects, 2, 5)
print("Subjects list after removing elements from index 2 to 4:", Subjects)
print()

# Step 8: Pop 5th element after reversing and sorting your list.
Subjects.reverse()
Subjects.sort()
element = Subjects.pop(4)
print(f"Popped 5th element '{element}' after reversing and sorting:", Subjects)
print()

total_elements = len(Subjects)
print("Total elements in Subjects list:", total_elements)
print()

# Step 9: Count total elements in your list and finally clear the list.
Subjects.clear()
print("Subjects list after clearing:", Subjects)
