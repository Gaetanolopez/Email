# define email class
class Email:
    # make 2 attributes
    has_been_read=False
    is_spam=False
    # initialize class
    def __init__(self,email_contents,from_address):
        self.email_contents=email_contents
        self.from_address=from_address
    # define method mark_as_read
    def mark_as_read(self):
        self.has_been_read=True
    # define method mark_as_spam
    def mark_as_spam(self):
        self.is_spam=True
    # str format allowes to read email from inbox as a string format  
    def __str__(self):
        return f'''
        \n Contents:{self.email_contents}
        \n From:{self.from_address}
        \n Read:{self.has_been_read}
        \n Spam:{self.is_spam}
        -------------------------------------------------------------------\n'''
# create list for email
inbox=[]
# define function to create email
def add_email():
    contents=input("Enter the contents \n")
    email_address=input("Enter email address \n")
    email=Email(contents,email_address)
    inbox.append(email)
# get hot many emails there are
def get_count():
    count=len(inbox)
    print(count)
# the user can choose the number of the email that is interested in
def get_email():
    i=int(input("Select the number of the email you want to retrieve \n"))
    get_email=inbox[i-1]
    get_email.mark_as_read()
    print(get_email)
   
# Display all the email not read yet
def get_unread_emails():
    no_read=list()
    for email in inbox:
        if email.has_been_read==False:
            no_read.append(email)
    for email in no_read:
        print(email)

# make a list of spam emails  
def get_spam_emails():
    spam=list()
    for email in inbox:
        if email.is_spam==True:
            spam.append(email)
    #print(spam)
    for email in spam:
        print(email)

# the user decides the index of the email that wants to delete
def delete():
    i=int(input("Write the index of the email you want to delete \n"))
    return inbox.pop(i)

# create string variable
user_choice = ""

# while loop that connects all the funcions above and stops when the user types quit
while user_choice != "quit":
    user_choice = input("What would you like to do - send/read/get unread email/spam email/mark spam/email count/delete/quit? \n")
    if user_choice == "send":
        add_email()
       
    elif user_choice == "read":
        for email in inbox:
            print(inbox.index(email)+1,email.from_address)
        get_email()
     
    elif user_choice=="get unread email":
        get_unread_emails()
       
    elif user_choice=="spam email":
        get_spam_emails()
         
    elif user_choice == "mark spam":
        i=int(input("Enter index of email to be marked as spam \n"))
        inbox[i].mark_as_spam()
       
    elif user_choice=="email count":
        get_count()
    elif user_choice=="delete":
        delete()
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")