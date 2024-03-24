#!/usr/bin/env python3


#The Agruement and variable
def create_email(user_id,domain):

    #Returning value, giving back that data and the user_id gets appended (@madisoncollege.edu) email address
    return user_id + "@" + domain

#Variable
username = "Rlanderson1"
domainname = 'madisoncollege.edu'

#Assign it to a variable.  Whatever gets 'returned' will get assigned to the variable.  Whatever the value of username is, it's going to get stored in the user_id
emailaddress = create_email(username,domainname)

#Should print username (Rlanderosn1) and user_id wich is @madisoncollege.edu
print(emailaddress)




#Define the imput function. Pistional agruements
#def format_name(firstname, lastname):

    #return f"First Name: {firstname} Last Name: {lastname}"

#Call the input function from in your code
#This won't do anything
#format_name("Rae", "Denruiter")

#This will retrieve the formatted string and print it
#print(format_name((Rae", "Denruiter))