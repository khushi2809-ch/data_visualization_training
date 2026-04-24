username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

'''output:
Enter username: admin
Enter password: 1234
Login Successful
Enter username: user
Enter password: pass
Invalid Credentials
'''
