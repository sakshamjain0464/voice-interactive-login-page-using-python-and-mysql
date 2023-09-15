import pyttsx3  #importing Speech Module
import pwinput as p #for password input
import verification as backend #Module for verification of credentials
from rich.console import Console  #terminal decoration

console = Console() #initialized console object

speech = pyttsx3.init() #initialized Speech Module

# Welcome Section
console.print("-------------------------------------------------------------------------------------------------------------------------------", style= 'green', justify="center")
console.print("\nWelcome to Login Page\n", style='red bold', justify='center')
console.print("-------------------------------------------------------------------------------------------------------------------------------", style= 'green', justify="center")
speech.say("Welcome to Login Page")
speech.runAndWait()
console.print("\n[bold green]You Want to:\n[/bold green][blue]1.)Press 1 to Login\n2.)Press 2 to SignUp\n3.)Press 3 to Change Password[/blue]")
speech.say("Press 1 to Login, Press 2 to SignUP, Press 3 to Change Password!")
speech.runAndWait()
n = int(input("-> "))


console.print("\n-----------------------------------------------------------------------------------------------", style='bold blue', justify="center")
# Login Part
if(n == 1):
    console.print("\nLogin\n", style='yellow', justify="center")
    console.print("\n-----------------------------------------------------------------------------------------------", style='bold blue', justify="center")
    i = 0
    while(True):
        speech.say("Enter Username")
        speech.runAndWait()
        username = input("Enter User-name : ")
        speech.say("Enter Password")
        speech.runAndWait()
        password = p.pwinput("Enter Password : ")
        if(backend.login(username, password) == True):
            console.print("\nLogged in Successfully!!!\n", style='green')
            speech.say("Logged in Successfully")
            speech.runAndWait()
            break
        else:
            if(i == 3):
                console.print("\nLogin Failed, Time Limit Exceeded, Please try after some time\n\n",style='red')
                speech.say("Login Failed, Time Limit Exceeded,  Please Try After some Time!!")
                speech.runAndWait()
                break
            else:
                console.print("\nInvalid Credentials, Please Try again\n", style='red')
                speech.say("Invalid Credentials, Please Try again!")
                speech.runAndWait()
                i+= 1

# SignUP part
elif (n == 2):
    console.print("\nSignUP\n", style='yellow', justify="center")
    console.print("\n-----------------------------------------------------------------------------------------------", style='bold blue', justify="center")
    i = 0
    while(True):
        if(i==3):
            console.print("SignUP Faild, Please Try After some Time", style='red')
            speech.say("SignUP Faild, Please Try After some Time")
            speech.runAndWait()
            break
        speech.say("Enter Username")
        speech.runAndWait()
        username = input("Enter User-name : ")
        speech.say("Enter Password")
        speech.runAndWait()
        password = p.pwinput("Enter Password : ")
        speech.say("Confirm Password")
        speech.runAndWait()
        con_password = p.pwinput("Confirm Password: ")
        if(password == con_password):
            if(backend.signUP(username, password) == True):
                console.print("SignUP Sucessful!!", style='green')
                speech.say("SignUP Successful, You can Now Login")
                speech.runAndWait()
                break
            else:
                console.print("Username Or Password is Already Taken", style='red')
                speech.say("Username Or Password is Already Taken")
                speech.runAndWait()
                i+=1
        else:
            console.print("Password and Confirm Password Does Not Match!", style='red')
            speech.say("Password and Confirm Password Does Not Match!")
            speech.runAndWait()
            i+=1

# Change Password Part
elif(n == 3):
    console.print("\nChange Password\n", style='yellow', justify="center")
    console.print("\n-----------------------------------------------------------------------------------------------", style='bold blue', justify="center")
    i = 0
    while(True):
        speech.say("Enter Username")
        speech.runAndWait()
        username = input("Enter User-name : ")
        speech.say("Enter Password")
        speech.runAndWait()
        password = p.pwinput("Enter Password : ")
        if(backend.login(username, password) == True):
            console.print("\nLogged in Successfully!!!\n", style='green')
            speech.say("Logged in Successfully\n")
            speech.runAndWait()
            speech.say("Enter New Password")
            speech.runAndWait()
            new_pwd = p.pwinput("Enter New Password: ")
            speech.say("Confirm New Password")
            speech.runAndWait()
            con_pwd = p.pwinput("Confirm New Password: ")
            if(new_pwd == con_pwd):
                if(backend.change(username, password, new_pwd) == True):
                    console.print("\nPassword Changed Successfully!!!\n", style='green')
                    speech.say("Password Changed Successfully")
                    speech.runAndWait()
                
                else:
                    console.print("\nPassword could not be updated\n", style='green')
                    speech.say("Password could not be updated")
                    speech.runAndWait()
            else:
                console.print("\nPassword and Confirm password doesnot match!\n", style='red')
                speech.say("Password and confirm password does not match")
                speech.runAndWait()
            break  
        else:
            if(i == 3):
                console.print("\nLogin Failed, Time Limit Exceeded, Please try after some time\n\n",style='red')
                speech.say("Login Failed, Time Limit Exceeded,  Please Try After some Time!!")
                speech.runAndWait()
                break
            else:
                console.print("\nInvalid Credentials, Please Try again\n", style='red')
                speech.say("Invalid Credentials, Please Try again!")
                speech.runAndWait()
                i+= 1