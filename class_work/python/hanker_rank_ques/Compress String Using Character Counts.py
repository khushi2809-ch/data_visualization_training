s = input()
result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)

'''output:
Enter a string: aaabbc
a3b2c1
Enter a string: hello
h1e1l2o1
'''
