## A module to store Restaurant and IceCreamStand classes
class Restaurant:
	def __init__(self, name, cuisine_type):
		""" Initialises the instance"""
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		""" Prints a descriptive phrase of the instance"""
		print(f"{self.name.title()} cooks {self.cuisine_type}")

	def set_number_served(self, num):
		""" Set number of served customers"""
		self.number_served = num

	def increment_number_served(self, num=1):
		""" Increments number of served customers by num"""
		if num >= 0:
			self.number_served += num
		else:
			print("Cannot roll back served customers")

class IceCreamStand(Restaurant):
	def __init__(self, name, cuisine_type, *flavours):
		""" Initialise attributes of parent class"""
		super().__init__(name, cuisine_type)
		self.flavours = flavours

	def describe_flavours(self):
		""" Prints a list of flavours """
		print(f"\nThe following flavours are sold by {self.name}\n")
		for flavour in self.flavours:
			print(f"\t{flavour.title()}")