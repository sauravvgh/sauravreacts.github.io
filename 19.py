#Write a Python program to get the smallest number from a list.
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the first element
print("Smallest element is:", *list1[:1])
