from curses.ascii import isalnum, isalpha
#from xxlimited import new
from qbay import app
from flask_sqlalchemy import SQLAlchemy

import string
import re
import random


'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


class User(db.Model):
    '''
    R1-8
        Shipping address is empty at the time of registration.
    R1-9
        Postal code is empty at the time of registration.
    R1-10
        Balance should be initialized as 100 at the time of registration. (free $100 dollar signup bonus).
    '''
    id = db.Column(db.Integer, nullable=False)
    # added default value for billing_address = ""
    billing_address = db.Column(db.String(150), default="",  nullable=False)
    # added default value of account_bal = 100
    account_bal = db.Column(db.Integer, default=100, nullable=False)
    # added default value of postal_code = ""
    postal_code = db.Column(db.String(20), default="", nullable=False)
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False, 
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# create all tables
db.create_all()



def register(name, email, password, billing_address, postal_code,account_bal):
    '''
    R1-7
        If the email has been used, the operation failed.
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
        billing_address (string): user billing address
        postal_code (string): user postal_code
        account_bal (integer): user account_bal
      Returns:
        True if registration succeeded otherwise False
    '''
    
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

 
    
    # create a new user
    user = User(username=name, email=email, password=password)
    if (email == "" and password ==""):
        return False
    # add it to the current database session
    db.session.add(user)
    db.session.commit()
    
    
    
    
    return True


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]


def update(name, email, billing_address, postal_code):
    '''
    R3-1
    A user is only able to update his/her user name, user email, billing address, and postal code
      Parameters:
        name (string): user name
        email (string): user email
        billing_address (string): user billing_address
        postal_code (string): user postal_code
    '''
    # checking if user data in database equals current user data in current session
    user = User.query.filter_by(User.username==name).all()
    if (user):
        # if yes, then update old user data in database
        update_helper(name, email, billing_address, postal_code)
    return False
    

def update_helper(name, email, billing_address, postal_code):
    '''
    R3-1
    helper function to update his/her user name, user email, billing address, and postal code
      Parameters:
        name (string): user name
        email (string): user email
        billing_address (string): user billing_address
        postal_code (string): user postal_code
    '''
    # accessing user data
    q = db.session.query(User)
    # check if user id is correct
    q = q.filter(User.id==1) # needed id generator
    # updating old user data
    record = q()
    record.name = name
    record.email = email
    record.billing_address = billing_address
    record.postal_code = postal_code
    # saving updates to database
    db.session.commit()

    return True
                    
#R1-2- A user is uniquely identified by his/her user id
def user_id_helper(user):
    #generate a random id for the user
    for i in range(len(user)):
        id = random.randint(1,1000)
    
    #check if the user id already exists
    existed = id.query.filter_by(user=user).first()


#R1-3
def email_helper(email):
    '''
    R1-1:
    Email cannot be empty. password cannot be empty.
    R1-3
    The email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for 
    a human-friendly explanation). You can use external libraries/imports.
      Parameters:
        email (string): user email
    '''
    
    regex = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{1,3}')
    #the email meets the requirements
    if (re.fullmatch(regex, email)): 
        return True
    else:
        return False
    
    
#R1-4
def password_helper(password):
    ''')
    R1-1:
    Email cannot be empty. password cannot be empty.
    R1-4:
    Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, 
    and at least one special character.
      Parameters:
        password (string): user password
    '''
    #lower case
    count_l = 0 
    #upper case
    count_u = 0 
    #special character
    count_s = 0 
        
    for ch in password:
        #uppercase characters
        if (ch.isupper()): 
            count_u+=1
        #lowecase characters
        if (ch.islower()): 
            count_l+=1
        #special character
        if ch in string.punctuation: 
            count_s+=1
        
    #check the validity of the password
    #password is not empty
    if (password != ""): 
        #the password has 6 or more characters
        if (len(password) >= 6):  
            #more than one uppercase, lowercase and special characters
            if (count_u >=1 and count_l >=1 and count_s >= 1):  
                return password
            else:
                return None
        else:
            return None
    else:
        return None
     
    
#R1-5 and 
def username_helper(username):
    '''
    R1-5:
        User name has to be non-empty, alphanumeric-only, and space allowed 
        only if it is not as the prefix or suffix.
    R1-6: 
        User name has to be longer than 2 characters and less than 20 characters.
    R3-1: 
        A user is only able to update his/her user name, user email, billing address, and postal code.
    R3-4: 
        User name follows the requirements above.
        (postal code should be non-empty, alphanumeric-only, and no special characters such as !)
    Parameters:
        username (string): user username
    '''
    #check for special characters
    last_ch = len(username)-1
    #username is not empty
    if (username != ""): 
        for ch in range(len(username)):
            #the first character and last character cannot be a space 
            if (username[0] != "" and username[last_ch] != ""): 
                #the username is alphanumeric
                if (username[ch].isalnum()): 
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False
    

#R3-1: 


#R3-2
def postal_code_helper(postal_code):
    '''
    R3-2
    postal code should be non-empty, alphanumeric-only, and no special characters such as !
    R3-3
    Postal code has to be a valid Canadian postal code
      Parameters:
        postal_code (string): user postal_code
    '''
    #special character
    count_s = 0
    #digits
    num_count = 0
    #alphabets
    char_count = 0
    
    for ch in range(len(postal_code)):
        #count the number of special characters
        if postal_code in string.punctuation:
            count_s += 1

        # checking if empty string
        if (postal_code[ch] != ""):
            # checking if letter
            if (ch == 0 or ch == 2 or ch == 4) and postal_code[ch].isalpha():
                char_count += 1
            # checking if number
            if (ch == 1 or ch == 3 or ch == 5) and postal_code[ch].isdigit():
                num_count += 1
    # checking if any special characters
    if (count_s == 0):
        # if 3 letters and 3 numbers
        if (num_count == 3 and char_count == 3):
            return True
        else:
            return False