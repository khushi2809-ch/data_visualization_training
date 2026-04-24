li = [1, 2, 2, 3, 4, 1, 5]

result = []

for i in li:
    if i not in result:
        result.append(i)

print(result)

'''output:
[1, 2, 3, 4, 5]
'''
