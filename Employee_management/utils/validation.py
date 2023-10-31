import re
from utils.input import Employee
from dateutil import parser
from models.db import DbConnect
from utils.log import Log
import utils.queries

class UserAlreadyExists(Exception):
    pass


class UserDoesNotExists(Exception):
    pass


class Validation:
    
    def phone_validator(func):
        def wrapper():
            while True:
                phone = Employee.new_phone()
                if Validation.is_valid_phone(phone):
                    result = func(phone)
                    return result
                else:
                    print(
                        "Your phone number should contain 10 digits exactly from 0-9.\n"
                    )
        return wrapper

    def is_valid_phone(phone):
        phone_pattern = r"^\d{10}$"
        return re.match(phone_pattern, phone) is not None
    
    @phone_validator
    def _check_phone_validity_(phone):
        print("Your phone number is valid!")
        return phone
    
    
    
    def is_valid_password(password):
        password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{6,}$"
        return re.match(password_pattern, password) is not None

    def password_validator(func):
        def wrapper():
            while True:
                password = Employee.new_password()
                if Validation.is_valid_password(password):
                    result = func(password)
                    return result
                else:
                    print(
                        "\nYour password should contain ATLEAST ONE UPPER CASE, ONE LOWER CASE and INTEGER VALUES and the LENGTH should be ATLEAST 6.\n"
                    )

        return wrapper

    @password_validator
    def _check_password_validity_(password):
        print("Valid password!")
        return password
    
    
    
    def check_date_format():
        while True:
            try:
                date = Employee.add_leave()
                parsed_date1 = parser.parse(date[0])
                parsed_date2 = parser.parse(date[1])
                formatted_date1 = parsed_date1.strftime('%Y-%m-%d')
                formatted_date2 = parsed_date2.strftime('%Y-%m-%d')
                if formatted_date1 > formatted_date2:
                    raise ValueError
                return [formatted_date1, formatted_date2]
            except ValueError:
                print("\nInvalid date format!\n")
        
        
    def check_input_details():
        while True:
            try:
                details = Employee.add_employee()
                value = Validation._is_user_exist(details['user_id'])
                if value == True:
                    Log.user_exist(details['user_id'])
                    raise UserAlreadyExists("\nThis user already exists\n")
                else:
                    break

            except UserAlreadyExists as e:
                print(e)
                print()
                
        details['Password'] = Validation._check_password_validity_()
        details['Phone'] = Validation._check_phone_validity_()
        return details
    
    def _is_user_exist(user_id):
        with DbConnect() as cursor:
            cursor.execute(
                utils.queries.IS_USER_EXIST,
                (user_id, ))
            result = cursor.fetchone()
            if result[0] == 1:
                return True
            return False
    
    
    def check_input_id():
        while True:
            try:
                user_id = Employee.remove_employee()
                value = Validation._is_user_exist(user_id)
                if value == False:
                    Log.user_not_exist(user_id)
                    raise UserDoesNotExists("This user does not exists")
                else:
                    break

            except UserDoesNotExists as e:
                print(e)
        return user_id
    
    def _is_user_exist(user_id):
        with DbConnect() as cursor:
            cursor.execute(
                utils.queries.IS_USER_EXIST,
                (user_id, ))
            result = cursor.fetchone()
            if result[0] == 1:
                return True
            return False
