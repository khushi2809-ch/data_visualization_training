s = input()
result = ""

for ch in s:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print(result)

'''output:
Enter a string: hello world
h*ll* w*rld
Enter a string: python programming
pyth*n pr*gr*mm*ng
'''
