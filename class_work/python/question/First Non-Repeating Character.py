s = "swiss"

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:", ch)
        break

'''output:
First non-repeating: w
'''
