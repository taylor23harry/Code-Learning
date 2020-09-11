## Module to store Admin class
from user import User

class Admin(User):
	def __init__(self, first_name, last_name, age, sex):
		""" Initialises attributes of parent class"""
		super().__init__(first_name, last_name, age, sex)
		self.privileges = ['post', 'delete', 'ban', 'kick']
		
	def show_privileges(self):
		print(self.privileges)