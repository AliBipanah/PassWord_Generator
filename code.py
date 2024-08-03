import string
import random
import os

os.system('cls')

defult_setting = {

    'lower' : True,
    'upper' : True,
    'symbol' : True,
    'number' : True,
    'space' : False,
    'length' : 8,
}
PRINT_LINE = ('-' * 100)


def get_input_for_change_setting(option, defult):


    while True:
        user_input = input(f'Defult setting is :  {option} : {defult} : ')
        user_input = user_input.lower()

        if user_input in ['', 'y', 'n']:
            if user_input in ['', 'y']:
                return True
            return False
        else:
            print("your inout invalid , please try again")
            print(PRINT_LINE)


def get_password_length(option, defult):

    while True:
        len_password = input(f'Defult setting is :  {option} : {defult} : ')

        if len_password == '':
            return defult
        
        if len_password.isdigit():
            number = int(len_password)
            if number >= 5 and number <= 20:
                return int(number)
            else:
                print("YOur Number should Bettwin [5-20]")
                print(PRINT_LINE)
        else:
            print("YOur Input must a number , Please try again")
            print(PRINT_LINE)

def show_defult_setting(setting):

    print("Please Enter => [YES : y and NO : n and Enter : y]")
    print(PRINT_LINE)
    for option, defult in setting.items():


        if option != 'length':
            setting[option] = get_input_for_change_setting(option, defult)
        else:
            setting[option] = get_password_length(option, defult)

def get_lower():
    return random.choice(string.ascii_lowercase)

def get_upper():
    return random.choice(string.ascii_uppercase)

def get_symbol():
    return random.choice(string.punctuation)

# def get_number():
#     return random.choice('0123456789')

def get_random_password(random_password):
    rand_pass = random.choice(random_password)

    if rand_pass == 'lower':
        return get_lower()
    
    if rand_pass == 'upper':
        return get_upper()
    
    if rand_pass == 'symbol':
        return get_symbol()
    
    if rand_pass == 'number':
        return random.choice('0123456789')
    
    if rand_pass == 'space':
        return ''


def generator_password(setting):

    len_pass = setting['length']
    final_password = ''

    choice = list(filter(lambda x : setting[x] == True, setting))

    # print(choice)

    for num in range(len_pass):
        final_password += get_random_password(choice)
    
    return final_password


def get_another_password(setting):

    while True:
        print(generator_password(defult_setting))
        print(PRINT_LINE)

        while True:
            user_input = input("Do You Want Another Password ? [Yes => y and No => n and Enter => y] : ")

            if user_input in ['', 'y', 'n']:
                if user_input in ['n']:
                    return
                break
            else:
                print("Your Input invalid, Please try again")

            


show_defult_setting(defult_setting)
print(PRINT_LINE)
(get_another_password(defult_setting))