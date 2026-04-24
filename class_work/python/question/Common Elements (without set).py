li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]

common = []

for i in li1:
    if i in li2 and i not in common:
        common.append(i)

print(common)

'''output:
[3, 4]
'''
