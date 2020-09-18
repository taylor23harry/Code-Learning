from random import choice

lottery = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
lucky_numbers = []
ticket_length = 3 #This is the length of characters used in the tickets. 
					# Setting this too high can easily crash your IDE/PC if
					# you aren't responsible. Your computer has to go 
					# through 15^ticket_length combinations.
					# ie: if you set it to 4, you will be going through
					# 15^4 = 50,625 combinations. 15^5 = 759,375
				  	
 """Generates lucky numbers """
for lucky in range(ticket_length):
	chosen = choice(lottery)
	lucky_numbers.append(chosen)

def find_win():
	""" Find winning ticket"""
	run = True
	attempt = 0
	print(f"Any ticket with the following numbers or letters wins a prize:\n\t {lucky_numbers}\n\n")
	while run == True:
		""" Randomly chooses 4 characters from 
		lucky_numbers and adds them to current_numbers"""
		current_numbers = []
		for n in range(ticket_length): 
			n = choice(lottery)
			current_numbers.append(n)
		""" Checks if randomly selected ticket matches the winning one."""
		if current_numbers == lucky_numbers:
			print(f"\nTicket found! after {attempt} attempts\n\t{lucky_numbers}\n")
			run = False
		else:
			print(f"{current_numbers}\n")
			attempt += 1		
			

class Ticket():
	""" Models a lottery ticket"""
	def __init__(self, *chosen_numbers):
		""" Initialises the  ticket attributes"""
		self.chosen_numbers = chosen_numbers

	def check_win(self):
		if self.chosen_numbers == lucky_numbers:
			print("Congratulations! You have the winning ticket!!")
		else:
			print("Sorry, better luck next time :(")



my_ticket = Ticket(5,2,'e','d')
find_win()