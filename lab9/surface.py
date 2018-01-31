import rectangle
class Surface:
	def __init__(self, filename, x, y, h, w):
		'''
		Constructs a surface object
		paramlist: filename (file name for image file), x (x coordinate), y (y coordinate), h (height), w (width)
		return: none
		'''
		self.image = filename
		self.rect = rectangle.Rectangle(x, y, h, w)
		
	def getRect(self):
		'''
		Returns a rectangle object based on the x, y, h, and w variables
		paramlist: none
		return: self.rect (the rectangle object)
		'''
		return self.rect
