#!/usr/bin/env python3

#Import the Console module
    #from rich.consoloe import Console
#Create a console object
    #console = Console()
#Use that object's print function to get more functionality
    #console.print("Hello :smiley:", stye="bold yellow")

from rich.console import Console

def create_email(user_id,domain="testdomain.edu"):

     return user_id + "@" + domain


def main():

     username = "Rlanderson1"
     domainname = 'madisoncollege.edu'
     console = Console
     emailaddress = create_email(username,domainname)
     print(emailaddress)
     console.print("Hello :smiley:", style="bold yellow")

   print(__name__)

if __name__ == "__main__":
    main()