#!/usr/bin/env python3

#The Agruement and variable
def create_email(user_id):

    #Returning value, giving back that data and the user_id gets appended (@madisoncollege.edu) email address
    return user_id + "@madisoncollege.edu"

#Variable
username = "Rlanderson1"

#Assign it to a variable.  Whatever gets 'returned' will get assigned to the variable.  Whatever the value of username is, it's going to get stored in the user_id
emailaddress = create_email(username)

#Should print username (Rlanderosn1) and user_id wich is @madisoncollege.edu
print(emailaddress)