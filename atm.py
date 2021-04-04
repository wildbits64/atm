# start of atm
import random

database = {}

def init():
    have_account = int(input('welcome, do you have acocunt with us: 1 (yes)  2 (no) \n')
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        init()

def login():
    print('login to your account \n')
    account_number_from_user = int(input('what is your account number? \n'))
    password_from_user = input('what is your password? \n')
    for account_number, user_details in database.item():
        if account_number == account_number_from_user:
            if user_details[3] == password:
                bank_operation(user_details)
    print('invalid account or password')
    login()

def register():
    print('registration information')
    email = input('what is your email ? \n')
    first_name = input('what is your first name ? \n')
    last_name = input('what is your last name ? \n')
    password = input('enter password \n')

    acocunt_number = generate_account_number()
    database[acocunt_number] = [first_name,last_name,email,password]
    
    print('your account has been created, please login')
    login()

def bank_operation():
    print('welcome %s %s' user[0],user[1])
    option = input('what would you like to do? (1) deposit (2) withdraw (3) logout \n')
    if option == 1:
        deposit()
    elif option == 2:
        withdraw()
    elif option == 3:
        init()
    
def withdraw():
    cash_selection = int(input('How much would you like to withdraw? \n'))
    if cash_selection:
        print('take your cash')
        break

def deposit():
    amount_to_deposit = int(input('How much would you like to deposit? \n'))
    if amount_to_deposit:
        current_balance += amount_to_deposit
        print('your new balance is ', current_balance)
        break

def generate_account_number():
    print('generating account number')
    return random.randrange(1111111111,9999999999)

# start atm screen
init()
