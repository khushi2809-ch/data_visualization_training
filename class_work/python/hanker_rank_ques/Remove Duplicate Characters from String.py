s = input()
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

'''output:
Enter a string: hello world
helo wrd
Enter a string: python programming
pythn ograim
'''
