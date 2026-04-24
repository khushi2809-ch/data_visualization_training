li = [1, 2, 3, 4, 5]
target = 6

pairs = []

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] + li[j] == target:
            pairs.append((li[i], li[j]))

print(pairs)

'''output:
[(1, 5), (2, 4)]
'''
