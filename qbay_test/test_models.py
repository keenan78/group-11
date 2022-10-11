from qbay.models import register, login, username_helper, postal_code_helper, update

def test_r1_7_user_register():
  '''
  Testing R1-7: If the email has been used, the operation failed.
  '''
  assert register('u0', 'test0@test.com', '123456') is True
  assert register('u0', 'test1@test.com', '123456') is True
  assert register('u1', 'test0@test.com', '123456') is False


def test_r1_8_user_register():
  '''
  Testing R1-8: Shipping address is empty at the time of registration.
  '''
  assert register('1', 'u0', 'test1@test.com', '123456', '', '', '100') is True
  assert register('1', 'u0', 'test1@test.com', '123456', '', '', '100') is True


def test_r1_9_user_register():
  '''
  Testing R1-9: Postal code is empty at the time of registration.
  '''
  assert register('1', 'u0', 'test1@test.com', '123456', '', '', '100') is True


def test_r1_10_user_register():
  '''
  Testing R1-10: Balance should be initialized as 100 at the time of registration. 
  (free $100 dollar signup bonus).
  '''
  assert register('1', 'u0', 'test1@test.com', '123456', '', '', '100') is True


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address 
      and the password.
    (will be tested after the previous test, so we already have u0, 
      u1 in database)
    '''
    user = login('test0@test.com', 123456)
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 1234567)
    assert user is None


def test_r1_5_username_helper():
   assert username_helper('jasondawn123') is True
   assert username_helper('bobrawn1') is True
   assert username_helper('john henry') is True
   assert username_helper(' huh-123') is False


def test_r1_6_username_helper():
    '''
    Testing R1-6: User name has to be longer than 2 characters and 
    less than 20 characters.
    '''
    user = username_helper('user123')
    assert user is not None

    user = username_helper('testinglongerusername')
    assert user is None


def test_r1_8_register():
  '''
  Testing R1-7: Shipping address is empty at the time of registration.
  '''
  assert register('0', 'u2', 'test0@test.com', '123456', '', 'L8K2G2', '0') is True
  assert register('0', 'u2', 'test0@test.com', '123456', 'bill ave', 'L0E8U8', '0') is False


def test_r1_10_register():
  '''
  Testing R1-10: Balance should be initialized as 100 at the time of registration. 
  (free $100 dollar signup bonus).
  '''
  assert register('0', 'u3', 'test0@test.com', '123456', '', 'L8K2G2', '100') is True
  assert register('0', 'u3', 'test0@test.com', '123456', '', 'L8K2G2', '0') is False


def test_r3_3_postal_code_helper():
  '''
  Testing P3-2: Postal code should be non-empty, alphanumeric-only, and 
  no special characters such as !.
  Testing R3-3: Postal code has to be a valid Canadian postal code.
  '''
  assert postal_code_helper('K7L3D4') is True
  assert postal_code_helper('L553NN') is False
  assert postal_code_helper('ABC ') is False
  assert postal_code_helper('') is False
  assert postal_code_helper('T_45C3!') is False

# def test_r3_1_update():
#   '''
#   Testing P3-1: A user is only able to update his/her user name, user email, 
#   billing address, and postal code
#   '''
#   #name
#   assert('','') is True
  
  
  #email
  #address
  #postal_code