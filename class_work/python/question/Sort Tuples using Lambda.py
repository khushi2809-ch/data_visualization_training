students = [("A", 85), ("B", 90), ("C", 75)]

sorted_list = sorted(students, key=lambda x: x[1])

print(sorted_list)

'''output:
[('C', 75), ('A', 85), ('B', 90)]
'''
