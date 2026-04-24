#---------------------
# list functions in python
#---------------------
# count(x) - Returns the number of times x appears in the list.
# reverse() - Reverses the order of the list.
# sort() - Sorts the list in ascending order.

# create a list of 20 numbers given by user
numbers = []

for i in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)

# displaying list
print("--------------------------")
print()
remove_num = int(input("Enter a number to remove from the list: "))

print("list is : ")
print(numbers)
print("--------------------------")

# frequency of a number in list
frequency = numbers.count(remove_num)

if frequency == 0:
    print(remove_num, "is not present in the list")

elif frequency == 1:
    print("as it is unique number, it will be removed from the list")
    numbers.remove(remove_num)
    print(numbers)

else:
    # reversing the list
    print("as it is not unique number, it will be removed except first occurrence")
    
    numbers.reverse()
    
    for i in range(1, frequency):
        numbers.remove(remove_num)   # value pass kiya
    
    # again reversing the list to maintain the original order
    numbers.reverse()
    
    print(numbers)