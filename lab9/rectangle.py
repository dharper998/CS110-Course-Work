class Rectangle:
	def __init__(self, x, y, h, w):
		'''
		Constructs the rectangle object
		Paramlist: x (x coordinate), y (y coordinate), h (height), w (width)
		return: none
		'''
		self.x = x
		self.y = y
		self.height = h
		self.width = w
		
	def __str__(self):
		'''
		Changes the string displayed when the rectangle object is printed
		Paramlist: none
		return: (x: self.x, y: self.y) width: self.width, height: self.height"
		'''
		return "(x: " + str(self.x) + ", y: " + str(self.y) + ") width: " + str(self.width) + ", height: " + str(self.height)
