n = int(input())
students = {}

for _ in range(n):
    name = input()
    marks = int(input())
    students[name] = marks

topper = max(students, key=students.get)
print(topper)

'''output:
Enter number of students: 3
Enter name of student: Alice
Enter marks of student: 85
Enter name of student: Bob
Enter marks of student: 90
Enter name of student: Charlie
Enter marks of student: 80
Bob
'''
