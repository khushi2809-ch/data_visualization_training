lst = list(map(int, input().split()))

if lst == lst[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

'''output:
Enter numbers: 1 2 3 2 1
Palindrome
Enter numbers: 1 2 3 4 5
Not Palindrome
Enter numbers: 1 2 2 1
Palindrome
Enter numbers: 1 2 3 4
Not Palindrome
'''
