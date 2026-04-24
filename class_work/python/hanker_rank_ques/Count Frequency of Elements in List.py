lst = list(map(int, input().split()))
freq = {}

for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

'''output:
Enter numbers: 1 2 3 2 4 1
{1: 2, 2: 2, 3: 1, 4: 1}
Enter numbers: 5 6 5 7 8 6
{5: 2, 6: 2, 7: 1, 8: 1}
Enter numbers: 1 1 1 1
{1: 4}
Enter numbers: 0 0 0 0
{0: 4}
'''
