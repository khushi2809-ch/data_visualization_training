li = [10, 20, 4, 45, 99]

largest = second = float('-inf')

for i in li:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)

'''output:
Second largest: 45
'''
