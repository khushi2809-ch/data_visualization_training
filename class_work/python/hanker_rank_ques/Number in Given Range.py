num = int(input("Enter a number: "))
low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))

if low <= num <= high:
    print("In Range")
else:
    print("Out of Range")

'''output:
Enter a number: 5
Enter lower bound: 1
Enter upper bound: 10
In Range
Enter a number: 15
Enter lower bound: 1
Enter upper bound: 10
Out of Range
'''
