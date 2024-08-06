# Start by creating a list named shopping_list containing the items: 'milk', 'eggs', 'bread', 'butter',
# Only then to realize, you have messed it up and now you need to fix it.

# First print the list and its first item.
shopping_list = ["milk","eggs","bread","butter"]

print(shopping_list)
print(shopping_list[0])

# Replace ‘bread‘ with ‘banana‘ (assume you don’t know where ‘bread’ is on the list and need to find the ‘bread’ index first).
bread_index = shopping_list.index("bread")
print(bread_index)

shopping_list[2] = "banana"
print(shopping_list)

# Insert 'apple' at the beginning of the shopping_list.
shopping_list.insert(0, "apple")
print(shopping_list)

# Add ‘flour’ and 'sugar’ items you forgot to add previously.

shopping_list.append("flour")
shopping_list.append("sugar")
print(shopping_list)

# Slice the list that includes only 'eggs' and 'banana'.
print(shopping_list[2:4])

# Print the list after every step.


