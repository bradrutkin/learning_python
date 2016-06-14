class Doppler_Calculator:
	c = 0
	V_r = 0
	V_s = 0
	f_0 = 0 
	

	def __init__(self):
		self.message()
		self.inputs()
		self.frequency()

	def message(self):
		print("This is the Doppler effect calculator.")
		print("Input your values and the program will report the observed frequency")
		print("Velocity of the reciever is negative if the reciever is moving away from the source")
		print("And vice versa. The same also applies to velocity of the source. The velocity is negative")
		print("if the source is moving away from the reciever")

	def inputs(self):

		'''
		Promps the user to input various values required for obtaining the observed 
		frequency.
		'''

		velocity_waves_medium = float(input("What is the velocity of the mediun? "))
		velocity_of_reciever = float(input("What is the velocity of the receiver? "))
		velocity_of_source = float(input("What is the velocity of the source? "))
		frequency_of_the_medium = float(input("What is the emitted frequency? "))
		self.c = velocity_waves_medium 
		self.V_r = velocity_of_reciever
		self.V_s = velocity_of_source
		self.f_0 = frequency_of_the_medium 

	def frequency(self):
		top = self.c + self.V_r
		bottom = self.c + self.V_s
		fraction = top/bottom
		observed = fraction * self.f_0
		print(observed)

a = Doppler_Calculator()


