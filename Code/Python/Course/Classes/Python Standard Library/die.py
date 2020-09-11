## Die class
from random import randint

class Die():
	def __init__(self, sides=6):
		""" Initialises the attributes of Dice"""
		self.sides = sides

	def roll_die(self):
		""" Rolls said die and returns value of roll"""
		rolled = randint(1, self.sides)
		print(f"\t{rolled}")

	def roll_times(self, times):
		""" Rolls a die numerous times"""
		self.times = times
		print(f"\nThe {self.sides} sided die is rolling:\n")
		for i in range(self.times):
			self.roll_die()


die = Die()
die.roll_times(10)

ten_sided_die = Die(10)
ten_sided_die.roll_times(10)

twenty_sided_die = Die(20)
twenty_sided_die.roll_times(10)

