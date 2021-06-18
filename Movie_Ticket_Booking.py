class project():
    import getpass
    def __init__(self):
        self.admin=open("administrator.txt","r")
        self.admin_a=open("administrator.txt","a")
        self.administrator_list=self.admin.readline().split()  #We Create A list With names of administors
        self.moviefile=open("movie.txt","r")                       #We Open A file named movie.txt to store all  the names of movies
        self.movies=self.moviefile.readline().split()                     #We Create a list of movie names for ease to  append new movies and remove existing
        self.moviefile.close()
        print'''--------Main Menu----------
        Signin          Enter 1
        Signup          Enter 2
        '''
        while True:     
            self.choice=input("Enter Your Choice:")
            if self.choice==1:                                     #If User Inputs 1 in Choice We redirect him to signin page
                import time
                print "Please Wait You Are Redirected To Signin Page"
                time.sleep(1.0)
                self.signin()
                break
            elif self.choice==2:                                   #if user Inputs 2 in Choice We redirect him to signup page
                import time
                print "Please Wait You Are Being Redirected To Signup Page...."
                time.sleep(1.0)
                self.signup()
                break
            else:                                                  #For Invalid Inputs
                print "Wrong Choice:"
                continue
    def signin(self):                                              #Function For Signin page
        print "Welcone to Signin Page..."
        self.username=raw_input("enter username: ")
        self.password=self.getpass.getpass("enter password: ")     #For Security purpose we input password in getpass function using getpass module
        self.file=open("database.txt","r")                         # database.txt stores all the information of users
        self.f=" "
        while len(self.f)>0:                                       #This loop checks for correct input of username and password and returns error for wrong inputs
           self.str=self.file.readline().split()
           if self.username in self.str:
               if self.password in self.str:
                   print""
                   print"Welcome ",self.username
                   print ""
                   if self.username in self.administrator_list:    #If username belong to administrator then he isredirected to special rights
                            print "You are a Administrator"
                            self.administrator()
                            break
                   else:
                        self.movie()
                        break
               else:
                   print"Incorrect Password"
                   self.signin()
           self.f=self.str
        else:
                print "Incorrect Username"
                self.newchoice=raw_input("Do You Want To Continue To Signin(y/n):")
                if self.newchoice=="y" or self.newchoice=="Y":
                     self.signin()
                elif self.newchoice=="n" or self.newchoice=="N":
                     self.signupchoice=raw_input("Do You Want To Signup(y/n)")
                     if self.signupchoice=="y" or self.signupchoice=="Y":
                         self.signup()
    def signup(self):#Functin For Signup
        self.filew=open("database.txt",'a')
        self.filer=open("database.txt",'r')
        self.fileu=open("username.txt",'a')
        self.fileur=open("username.txt",'r')
        print "Welcome To Signup Page"
        self.name=raw_input("Enter Your Name:")
        self.username=raw_input("Enter Username:")
        self.str=self.fileur.readline().split()
        if self.username in self.str:
            print "You Are Already a user"
            self.signin()
        else:
             self.filew.write('\n'+self.name)
             self.fileu.write('\t'+self.username)
             self.filew.write('\t'+self.username)
             self.password=self.getpass.getpass("Enter Password:")
             self.filew.write('\t'+self.password)
             self.mobile=raw_input("Enter Mobile Number:")
             self.filew.write('\t'+self.mobile)
             self.filer.close()
             self.filew.close()
             if self.username in self.administrator_list:
                 print"Administrator Permission Granted to",self.username
             else:
                 import time
                 time.sleep(1.0)
                 print "You Are Succesafully Registered"
                 print "Please Signin To Continue"
                 self.signin()
    def movie(self):                                               # The Main Function To Dislay Movies And ask user to choose from
        print "----------movies now showing-----------"
        for n in range(len(self.movies)):
            print str(self.movies[n])+"-"*(30-len(self.movies[n]))+"enter ",n+1
        print "back-----------------------enter 9"                 #Name of movies are printed here
        print ""
        self.a= '''
    ---------------------Timings-----------------------
    10:00 AM - 1:00 PM -------------------Enter 1
    2:00 PM - 5:00 PM ---------------------Enter 2
    6:00 PM - 9:00 PM ---------------------Enter 3'''              #Timings of movies are printed here
        while True:
            self.choice=int(raw_input("enter your choice: "))
            if self.choice<>9:
                print self.a
                while True:
                    self.time=int(raw_input("choose your time:"))
                    if self.time==1:
                        self.filew=open(str(self.movies[self.choice-1])+"_1.txt","a")
                        self.filer=open(str(self.movies[self.choice-1])+"_1.txt","r")
                        break
                    elif self.time==2:
                        self.filew=open(str(self.movies[self.choice-1])+"_2.txt","a")
                        self.filer=open(str(self.movies[self.choice-1])+"_2.txt","r")
                        break
                    elif self.time==3:
                        self.filew=open(str(self.movies[self.choice-1])+"_3.txt","a")
                        self.filer=open(str(self.movies[self.choice-1])+"_3.txt","r")
                        break
                    else:
                        print""
                        print "invalid choice"
                break
            elif self.movie==9:
                self.signin()
            else:
                print""
                print"invalid choice"
                self.ask=raw_input("do you want to continue(Y/N): ")
                if self.ask=="y" or self.ask=="Y":
                     print ""
                else:
                    break
        self.seat_booking()
    def seat_booking(self):                                  #Function To Ask User To Choose His/Her Seats
        self.z=(self.filer).readline()
        self.seats=open("seats.txt","a")
        self.seats=open("seats.txt","r")
        self.y=(self.seats).readlines()
        print""
        print '''  ------------Your Screen This Way-----------'''
        for n in range(len(self.y)):                         #Loop To print all the seats and hide the seats which are already booked
            self.x=self.y[n].split()
            self.st=""
            for m in self.x:
                if m in self.z:
                    self.st+="   **"
                else:
                    self.st+="   "+m
            print self.st
        print ""
        while True:
            self.ask=int(raw_input("enter no. of seats(max 8):  "))
            if self.ask>8:
                print "Sorry! You Can Book Maximum OF 8 Seats Only"
            else:
                break
        self.seats_no=1
        self.s=""
        for n in range(self.ask):
            self.choose=raw_input("choose your seat "+str(self.seats_no)+": ")
            self.u=self.choose.upper()
            while True:
                if self.u in self.z:
                    print "Seat Already Booked"
                elif (ord(self.u[0])-64)>7:
                    print "Invalid Seat"
                elif self.u in self.s:
                    print "Seat Already Chosen"
                elif len(self.u)>2:
                    print "Invalid Seat"
                elif self.u.isalnum()==False:
                    print "Invalid Seat"
                else:
                    self.s+=(" "+self.u)
                    (self.filew).write("\t"+self.u)
                    break
                self.choose=raw_input("choose your seats"+str(self.seats_no)+": ")
                self.u=self.choose.upper()
            self.seats_no+=1
        self.filer.close()
        self.filew.close()
        self.seats.close()
        self.show_info()
    def show_info(self):                           #Final Function to print all the details and fare
        self.fare=120
        import time
        print""
        time.sleep(0.5)
        print "Processing Your Request Please Wait...."
        time.sleep(2.0)
        print "seats you have booked are: ",self.s
        print "cost per seat: Rs ",self.fare
        print "Total amount: Rs ",self.ask*self.fare
        import random
        print "Tickets Successfully Booked"
        time.sleep(0.5)
        print "Your Ticket Code Is:",random.randint(10000,99999)
        time.sleep(1.0)
        print '''
    YOU ARE REQUESTED TO REACH THE TICKET COUNTER
    30 MINUTES PRIOR TO THE MOVIE TIMING
    RECIEVE TICKETS BY SHOWING YOUR TICKET CODE
    INCASE DELAY ,YOUR TICKET SHALL BE CANCELLED
    '''
        print"--------------------THANK YOU----------------------"
        print""
        self.quit_t()
    def administrator(self):                     #Adminstrator Function with Special Rights
        print '''-----------Choose a operation to Perform--------------------

        1.Add Movie Name.------------Enter 1
        2.Remove Movie Name.-------Enter 2
        3.Add Administrator.-----------Enter 3
        4.Update Fare.-------------------Enter 4
        5.Quit-----------------------------Enter 9
        '''
        self.perform=int(raw_input("choose operation to perform: "))
        if self.perform==1:                      #To add new Movie
            self.new_movie=raw_input("Enter Movie To Add:")
            self.moviefile=open("movie.txt","a")
            self.movies.append(self.new_movie)
            self.moviefile.write("\t"+self.new_movie)
            self.moviefile.close()
            print "Movie Added Successfully!!!"
            self.administrator()
        elif self.perform==2:                   #To remove Existing movie
           print "Here are existing Movie Names:"
           for i in range(len(self.movies)):
               print self.movies[i]
           print""
           self.remove_movie=raw_input("Enter Movie To be Removed From List:")
           self.movies.remove(self.remove_movie)
           self.moviefile=open("movie.txt","w")
           self.moviefile.write(self.movies[0])
           self.moviefile=open("movie.txt","a")
           for i in range(1,len(self.movies)):
               self.moviefile.write('\t'+self.movies[i])
           self.moviefile.close()
           print "Movie Successfully Removed!!!"
           self.administrator()
        elif self.perform==3:                   #To add new administrator
            self.fileur=open("username.txt","r")
            self.admin_r=open("administrator.txt","r")
            self.file_user_readlines=self.fileur.readline().split()
            self.admin=open("administrator.txt","a")
            self.new_admin=raw_input("Enter Username of new admin:")
            while True:
                if self.new_admin in self.administrator_list:
                    print "Sorry The user is already a admin"
                    break
                elif self.new_admin in self.file_user_readlines:
                    self.administrator_list.append(self.new_admin)
                    self.admin.write("\t"+self.new_admin)
                    print"Administrator Permission Granted to",self.new_admin
                    break
                else:
                    self.administrator_list.append(self.new_admin)
                    print"The user is not pre-existing"
                    print "you are redirected to signup page....."
                    self.signup()
                    self.admin.write("\t"+self.username)
                    break
            self.fileur.close()
            self.admin.close()
            self.administrator()
        elif self.perform==4:                  #To change Fare rates
            self.newfare=int(raw_input("Enter New Fare :Rs "))
            self.fare=self.newfare
            print "Fare Changed to Rs.",self.fare
            self.administrator()
        elif self.perform==9:                 #To exit the function
            print "Your Changes Are Saved"
            self.signin()
        else:                                #If user inputs a wrong entry
            print "Wrong Entry"
            self.administrator()
    def quit_t(self):
        self.enter=raw_input("Press Any Key To Quit:")
        quit()
obj=project()
                                                                                                                                                                                      