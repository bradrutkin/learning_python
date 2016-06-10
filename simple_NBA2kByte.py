import random

class NBA2kByte:
	
	def __init__(self):
		self.run_game()
		self.setup_player()

	def run_game(self):
		print("Congrats on being drafted 1st overall! Will you have what it takes to win rookie of the year?")
		print("You will first be prompted to select a name. Then carefully choose how you skill your player  The five categories are shooting, passing, defense, aggressiveness and speed")
		print("Each category is based off from 1-10. 1 is the worst and 10 is the best. You have 30 attribute points to spend.")

	def setup_player(self):
		player = Player()
		skills = Skill()
		# results = Skill.results(self)


class Player:
	def __init__(self):
		self.name = self.name_gen()

	def name_gen(self):
		name_answer = str(input("Would you like to use the random name generator...Y or N? "))
		if name_answer[0].lower() == str("y"):
			name = ""
			first_names = ['Lebron', 'Brad', 'Kobe', 'Steph', 'Michael','Wilt']
			last_names = [' James', ' Rutkin', ' Bryant', ' Curry', ' Jordan',' Chamberlin']
			name += (random.choice(first_names))
			name += (random.choice(last_names))
			print ("Your name is", name)
			return (name)
		elif name_answer[0].lower() == "n":
			name = str(input("What is your name? "))
			return (name)
		else:
			print("Please type y for yes or n for no.")

class Skill:

	skill_points = 25

	ppg = 0 
	spg = 0
	rpg = 0
	apg = 0

	rookie_of_the_year_counter = 0


	def __init__(self):
		self.shooting = self.shooting()
		self.defense = self.defense()
		self.aggressiveness = self.aggressiveness()
		self.passing = self.passing()
		self.results = self.results()

	def shooting(self):
		while True:
			print("How many skill points would you like to add to shooting?")
			shooting = (input("Please enter a whole number value from 1 to 9: "))
			if  47 <= ord(shooting) <= 57:
				if 1 <= int(shooting) <= 9:
					print("Your shooting skill is: ", shooting)
					break
			else:
				print("Error")
		self.skill_points = self.skill_points - int(shooting)
		ppg_multiplier = random.uniform(1, 4.5)
		points_per_game = (int(shooting) * ppg_multiplier)
		self.ppg += points_per_game
		print("Your points per game in your rookie year will be:", points_per_game)


	def defense(self):
		while True:
			print("How many skill points would you like to add to Defense?")
			print("You have", self.skill_points, "remaining.")
			defense = input("Please enter a whole number value from 1 to 9: ")
			if 47 <= ord(defense) <= 57:
				if 1 <= int(defense) <= 9:
					print("Your defense skill is: ", int(defense))
					break
			else:
				print("Error")

		steals_multiplier = random.uniform(1, 2.5)
		steals_per_game = (float(defense)) * steals_multiplier
		self.skill_points = self.skill_points - float(defense)
		self.spg = steals_per_game
		print ("Your steals per game during your rookie year will be: ", steals_per_game)

	def aggressiveness(self):
		while True:
			## Eventually I would like to adjust so that I can say how aggresive is your player's name 
			print("How aggressive is your player?")
			print("You have", self.skill_points, "remaining.")
			rebounds = input("Please enter a whole number value from 1 to 9: ")
			if 47 <= ord(rebounds) <= 57:
				if int(rebounds) <= self.skill_points:
					if 1 <= int(rebounds) <= 9:
						print("Your defense skill is: ", int(rebounds))
						break
				else:
					print("Error...you don't have that many skill points remaining")
			else:
				print("Error")
		rebounds_multiplier = random.uniform(1, 2.5)
		rebounds_per_game = (float(rebounds)) * rebounds_multiplier
		self.skill_points = self.skill_points - float(rebounds)
		self.rpg = rebounds_per_game
		print ("Your rebounds per game during your rookie year will be: ", rebounds_per_game)

	def passing(self):
		while True:
			## Eventually I would like to adjust so that I can say how aggresive is your player's name 
			print("How team orriented is your player?")
			print("You have", self.skill_points, "remaining.")
			passing = input("Please enter a whole number value from 1 to 9: ")
			if 47 <= ord(passing) <= 57:
				if int(passing) <= self.skill_points:
					if 1 <= int(passing) <= 9:
						print("Your defense skill is: ", int(passing))
						break
				else:
					print("Error...you don't have that many points remaining")
			else:
				print("Error")
		passing_multiplier = random.uniform(1, 2.5)
		assits_per_game = (float(passing)) * passing_multiplier
		self.skill_points = self.skill_points - float(passing)
		self.apg = assits_per_game
		print ("Your assits per game during your rookie year will be: ", assits_per_game)

	def results(self):

		if self.ppg >= 16:
			self.rookie_of_the_year_counter += 1
			#print(self.points_per_game)
		else:
		 	self.rookie_of_the_year_counter += 0 
		if self.apg >= 7:
			self.rookie_of_the_year_counter += 1
		else:
			self.rookie_of_the_year_counter += 0
		if self.rpg >= 7:
			self.rookie_of_the_year_counter += 1
		else:
			self.rookie_of_the_year_counter += 0
		if self.spg >= 7:
			self.rookie_of_the_year_counter += 1
		else:
			self.rookie_of_the_year_counter += 0

		if self.rookie_of_the_year_counter == 4:
			print("Congradulations...all the hard work has paid off and you are the NBA Rookie of The Year")
		else:
			print("Unfortanetly you underperformed, and did not win rookie of the year. Devastated, you retire and sign up for Byte Academy.")










# 	this runs the function 
if __name__ == '__main__':
	a = NBA2kByte()
