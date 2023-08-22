class Account():
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def checkpassword(self,password):
        return self.password == password
accounts=[ ]

loginaccount = None
while True:
    print("1.Create an Account:\n2.Login")
    choice =int(input("Select the option: "))
    if choice == 1:
        username= input("Enter username: ")
        password= input("Enter your password: ")
        accounts.append(Account(username,password))
        print("Hello " f"{username} You'r Account has been created successfully continue to login you'r Account")    
    elif choice ==2:
        username= input("Enter username: ")
        password= input("Enter your password: ")
        for account in accounts:
            if account.username == username and account.checkpassword(password):
                loginaccount = account
                #print(f"{username} is login successfully")
                break
        if loginaccount is None:
            print("Invaid username or password please enter valid username or password")
        else:
            print("Hello " f"{username} welcome to railway ticket reservation system  please book you'r tickets")
            break  
    else:
        print("Enter valid option")