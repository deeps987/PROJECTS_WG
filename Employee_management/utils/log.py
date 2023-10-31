import logging

class Log:
    
    def __init__(self):
        logging.basicConfig(filename='app.log', level=logging.INFO)
        
    def change_phone(self):
        logging.info(
                    'User with id %r has changed its phone number successfully!',
                    self.user_id)
        
    def change_password(self):
        logging.info(
                    'User with id %r has changed its password successfully!',
                    self.user_id)
        
    def add_leave(self):
        logging.info(
                    'User with id %r has requested for leave!',
                    self.user_id)
        
    def user_exist(self):
        logging.error(
                    "User with user_id %r already exists but was trying to get added again. ", 
                    self)
        
    def add_employee(self):
        logging.info(
                    'User with id %r has been added!',
                    self['user_id'])
        
    def user_not_exist(self):
        logging.error(
                    "User with user_id %r does not exists but was trying to get removed. ", 
                    self)
        
    def remove_employee(self):
        logging.info(
                    'User with id %r has been removed!',
                    self)