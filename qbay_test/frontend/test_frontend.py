from unittest.mock import patch

from qbay.models import User
from qbay_test.conftest import base_url
from seleniumbase import BaseCase

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):

    def test_1_login_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """

        # insert the register function here:
    
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "test0@test.com")
        self.type("#name", "Bob")
        self.type("#password", "Bobfill#12")
        self.type("#password2", "Bobfill#12")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test0@test.com")
        self.type("#password", "Bobfill#12")
        # click enter button
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Bob !", "#welcome-header")
    
    def test_2_updateUser_input(self, *_):
        # Check postal code
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test0@test.com")
        self.type("#password", "Bobfill#12")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID postal code --> not the correct format
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "LAA2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID postal code --> empty
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "")
        # click enter button
        self.click('input[type="submit"]')

        # VALID
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # Check billing address

        # INVALID billing address --> empty
        self.open(base_url + '/updateUser')
        # fill username, email, billing address 
        # and postal code
        self.type("#username", "Bob")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # VALID
        self.open(base_url + '/updateUser')
        # fill username, email, billing address 
        # and postal code
        self.type("#username", "Bob")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "1411 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # Open the home page
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Bob !", "#welcome-header")

    def test_3_updateUser_output(self, *_):
        # Check username
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test0@test.com")
        self.type("#password", "Bobfill#12")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID username
        # The username is greater than 20 characters
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "BobFiller1234567891011")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID username
        # There is a space in the begining
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", " Bob123")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID username
        # The username has an "!" at the end --> not alphanumeric
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob123!")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # VALID username
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob1234")
        self.type("#email", "test0@test.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')
        
        # Open the home page
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Bob1234 !", "#welcome-header")

    def test_4_updateUser_functionality(self, *_):
        # Check email
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test0@test.com")
        self.type("#password", "Bobfill#12")
        # click enter button
        self.click('input[type="submit"]')
        
        # INVALID email --> "_" in domain
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob")
        self.type("#email", "bob_fill12@gma_il.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID email --> empty
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob")
        self.type("#email", "")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID email --> Email is has more than 3 letters after "." 
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob")
        self.type("#email", "bob_fill12@gmail.come")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # VALID
        # open user update page
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Bob")
        self.type("#email", "bob_fill@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "bob_fill@gmail.com")
        self.type("#password", "Bobfill#12")
        # click enter button
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Bob !", "#welcome-header")

        

  
    


    
