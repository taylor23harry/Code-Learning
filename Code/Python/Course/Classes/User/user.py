## Module to store User class
class User:
	def __init__(self, first_name, last_name, age, sex):
		""" Initialize attributes for the instance"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.login_attempts = 0

	def describe_user(self):
		""" Prints a description of the user"""
		print(f"{self.first_name.title()} {self.last_name.title()} is a {self.age} year old {self.sex}.\n")

	def greet(self):
		""" Greets the user"""
		print(f"Hello {self.first_name.title()}. Welcome to PiedPiper!\n")

	def increment_login_attempts(self):
		""" Increments login attempts by num"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Admin(User):
	def __init__(self, first_name, last_name, age, sex):
		""" Initialises attributes of parent class"""
		super().__init__(first_name, last_name, age, sex)
		self.privileges = ['post', 'delete', 'ban', 'kick']
		
	def show_privileges(self):
		print(self.privileges)


