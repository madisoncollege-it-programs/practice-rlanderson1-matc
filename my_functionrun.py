#!/usr/bin/env python3

#When executed directly the main() function will get called:
# Test if the script has been run direcyly or if it has been inported
#Built in the value of that variables such as __name__ (you have to define 'name' to determin how a script is being run
#if __name__ == "__main__":
    # main()

    #If executed directly _name_is set to "_main"
    #if imported, _name_ will contain the module name

def create_email(user_id,domain="testdomain.edu"):

     return user_id + "@" + domain

def main():

     username = "Rlanderson1"
     domainname = 'madisoncollege.edu'

     emailaddress = create_email(username,domainname)
     print(emailaddress)
     print(create_email('test1'))

print(__name__)

if __name__ == "__main__":  #Being run directly
    main()


#Example:  A python script with a function
#def print_my_name():
    #name = input("Tell me your name:")
    #print("You said your name is: ", name)

#def main():
    #print_my_name()

#if __name_ == "__main":
   # main()