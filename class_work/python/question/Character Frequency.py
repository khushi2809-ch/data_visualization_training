s = "hello"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

'''output:
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
'''
