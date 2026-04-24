s = input()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])

'''output:
Enter a string: abc
a
ab
abc
b
c
Enter a string: hello
h
he
hel
hell
e
l
l
o
'''
