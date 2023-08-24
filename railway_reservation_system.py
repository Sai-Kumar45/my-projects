class Account():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def checkpassword(self,password):
        return self.password == password
    
class traininfo():
    def __init__(self,train_num,destination,avl_seats,source):
        self.train_num = train_num
        self.destination = destination
        self.avl_seats = avl_seats
        self.source = source

    def displayinfo(self):
        print("---------------")
        print(f"train_num:{self.train_num}")
        print(f"train_destination :{self.destination}")
        print(f"train_avl seats : {self.avl_seats}")
        print(f"train_source : {self.source}")       
        print("-----------------")

class Passenger():
    def __init__(self,p_name,p_age,p_mobile_number):
        self.p_name = p_name
        self.p_age = p_age
        self.p_mobile_number = p_mobile_number

    def  displayinfo(self):
        print("--------------")
        print(f"p_name:{self.p_name}")
        print(f"p_age:{self.p_age}")
        print(f"p_mobile_number : {self.p_mobile_number}")       
        print("-----------------")

accounts=[ ]

loginaccount = None
while True:
    print("1.Create an Account:\n2.Login:")
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
            print("Hello " f"{username} you'r login successfully! \nwelcome to railway ticket reservation system  please book you'r tickets")
            print("-------------------------------------------------------")
            break  
    else:
        print("Enter valid option")

#if loginaccount is not None:
trains =[traininfo(123456,"hyd",130,"peddavaram"),
            traininfo(122556,"vij",150,"nandhigama")]



while True:
    user_input = input(" Enter 1: to see Train Details , Enter 2: to Exit \n")
    if int(user_input) == 1:
        for train in trains:
           train.displayinfo()
        train_number = int(input("enter tarin Number:"))
        for i in range(len(trains)):
            if train_number == trains[i].train_num:
                print("Available ticket for this Train is:",trains[i].avl_seats)

                tickets = int(input("enter number of tickets to purchase:"))
                if  tickets <= trains[i].avl_seats:
                    passenger_name = input("Enter passenger name:")
                    passenger_age  = int(input("Enter your age:"))
                    passenger_number = int(input("enter your mobile number:"))

                    p = Passenger(passenger_name,passenger_age,passenger_number)
                    print(tickets,"have been booked :")
                    p.displayinfo()
                    trains[i].avl_seats = trains[i].avl_seats-tickets
                    print(trains[i].avl_seats,"availble seats")
                else:
                    print("sufficient tickets are not avilable:")

    elif int(user_input) == 2:
        break