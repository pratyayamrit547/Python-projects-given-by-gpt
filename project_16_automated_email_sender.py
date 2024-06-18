import smtplib
from email.message import EmailMessage
import re


# These three inbuilt libraries are important for automated email sender
# 1.SMTP(simple mail transfer protocol) it is essential for transfer of email on internet and
# 2. emailmessage which gives us framework for it
# 3.re is regular expression library which I will use for verification


class Automated_email_sender:
    """Here we have made a class for Automated email sender as we are trying to get same information
     more than 2 times that's why for making my code DRY I have used class"""

    def __init__(self):
        """This function has to get the information from the user like his email,receivers email, password,etc.
        This function will run as a template for the user"""
        # Getting the sender's email of the user
        self.sender_email = input("Provide sender's email:")
        # here we are calling number_of_users() because some users wants to message same message to many people
        self.receivers = self.number_of_receiver_email()
        # here we are getting subject for the email and body of it and taking the password
        # from the user for it's email
        self.subject = input("Give the subject for your email:\n")
        self.message = input("Type your Email body(message):\n")
        self.password = input("Password of sender's email:")
        # Here we are calling the EmailMessage() class for setting up the information from the user
        # in framework of emailmessage
        self.email = EmailMessage()
        self.email["From"] = self.sender_email
        self.email["To"] = ','.join(self.receivers)
        self.email['Subject'] = self.subject
        # here email.set_content is used for putting the body of email in emailmessage framework
        self.email.set_content(self.message)
        # here we are making the all email_email content in string for avoiding any unexpected error
        self.a = self.email.as_string()
        self.email_checker()

    def email_checker(self):
        """THIS FUNCTION HAS TO CHECK THE SENDER'S EMAIL. IS THE EMAIL INVALID OR NOT?"""
        # this is the raw pattern for matching
        pattern = r'^[a-z]*+[0-9]*?@+[a-z]*+\.+[a-z]*'
        check_for_sender = re.search(pattern, self.sender_email)
        if not check_for_sender == None:
            return self.option_for_user()
        else:
            print("THE SENDER'S EMAIL IS INVALID")

    def email_sending_system(self, smtp_server, smtp_port):
        """This function will run for both Gmail and Outlook as it get it's smtp server and port as its parameter"""

        try:
            # Here we are calling SMTP in smtplib for establishing a secure connection to outlook by the help of smtp port
            smtp = smtplib.SMTP(smtp_server, port=smtp_port)
            # Here we are starting the smtp by starttlls()
            smtp.starttls()
            # here we are doing the login process in chosen email
            smtp.login(self.email['From'], self.password)
            # here we are drafting the email
            smtp.sendmail(self.email['From'], self.email['To'], self.message)
            # here we are closing our connection and we are logging out from chosen Email
            smtp.quit()
            print("Email sent successfully!")
        # It will find any authentication problem given email by the user
        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate. Check your email and password.")
        # It will find error in Smtp and tell the problem to user
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

    def regex(self,email):
        pattern = r'^[a-z]*+[0-9]*?@+[a-z]*+\.+[a-z]*'
        a = re.search(pattern, email)
        if a!=None:
            self.option_for_user
        else:
            print("not ok")


    def number_of_receiver_email(self):
        """ THis function has just to check only how many receivers will get email from the user"""
        list_of_receivers = []
        try:
            ask_user = int(input("Type [1] for single receiver and [2] for multiple receiver:"))
            if ask_user == 1:
                receivers_email = input("Give receiver's address:")
                list_of_receivers.append(receivers_email)
            elif ask_user == 2:
                receivers_email = input("Give receiver's address:")
                list_of_receivers.append(receivers_email)
                while True:
                    ask = input(
                        'Type [Q] for quiting the adding the name of receiver\'s address and press any thing for avoiding quit option: ').title()
                    if ask == "Q":
                        break
                    else:
                        receivers_email = input("Give receiver's address:")
                        list_of_receivers.append(receivers_email)
            else:
                print("Give your input only in 1 and 2")
        except Exception as e:
            print("Type only in integer not any other data type")
            quit()
        return list_of_receivers

    def option_for_user(self):
        """This is the function we are giving option to the user"""
        try:
            ask_user = int(input(
                "Type [1] for sending through Outlook\nType [2] for sending email through Gmail\nType 1 or 2 for choosing sender's email:"))
            if ask_user == 1:
                # here we are given smtp server and port for Outlook
                smtp_server = "smtp-mail.outlook.com"
                smtp_port = 587
                self.email_sending_system(smtp_server, smtp_port)
            elif ask_user == 2:
                # here we are given smtp server and port for Gmail
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                self.email_sending_system(smtp_server, smtp_port)
            else:
                print("Type only 1 and 2")
        except ValueError:
            print("Type only in integer not any other data type")


print("Hello! Welcome to automated email sender")

email_sender = Automated_email_sender()
