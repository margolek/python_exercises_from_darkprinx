

class Car:

	def __init__(self,color,model,engine_version,speed,speedlim):
		self.color = color
		self.model = model
		self.engine_version = engine_version
		self.speed = speed
		self.speed_lim = speedlim

	def drive_ahead(self):
		return 'You drive ahead'

	def drive_backwards(self):
		return 'You drive backwards'

	def turn_left(self):
		return 'You turn left'

	def turn_right(self):
		return 'You turn right'

	def speed_limit(self):
		if self.speed > self.speed_lim:
			return 'Slow down'
		else:
			return 'Your speed is right'

myobject = Car('red','Mercedes','3.0',120,90)
a = myobject.speed_limit()
print(a)
