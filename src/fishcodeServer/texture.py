#!/usr/bin/env/ python3

class Texture(object):

	def __init__(self, size):
		self.size = size
		self.pixels = [[(0, 0, 0) for i in range(size[1])] for i in range(size[0])]

	def setPixel(self, pos, color):
		if pos[0] < self.size[0] and pos[1] < self.size[1]:
			self.pixels[pos] = color

	def getPixel(self, pos):
		return self.pixels[pos]

	def getWidth(self):
		return self.size[0]

	def getHeight(self):
		return self.size[1]

	def generateDefaultImg(self):
		for x in range(self.getWidth()):
			for y in range(self.getHeight()):
				self.pixels[x][y] = (255/self.getWidth()*x, 255/self.getHeight()*y, (255/self.getWidth()*x + 255/self.getHeight()*y)/2)

	def render(self):
		return self.pixels

	def toSerializible(self):
		return {"size":self.size, "pixels":self.pixels}
