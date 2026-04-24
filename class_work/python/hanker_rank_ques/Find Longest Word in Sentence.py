s = input()
words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

'''output:
Enter a sentence: Hello world
Hello
Enter a sentence: Python programming is fun
programming
Enter a sentence: Find longest word in this sentence
sentence
Enter a sentence: SingleWord
SingleWord
'''
