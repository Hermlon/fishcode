#!/usr/bin/env/ python3
class Location(object):

	def __init__(self, position=(0, 0), rotation=0):
		self.position = position
		self.rotation = rotation

	def setPosition(self, position):
		self.position = position

	def getPosition(self):
		return self.position

	def setX(self, x):
		self.position[0] = x

	def getX(self):
		return self.position[0]

	def setY(self, y):
		self.position[1] = y

	def getY(self):
		return self.position[1]

	def setRotation(self, rotation):
		self.rotation = rotation

	def getRotation(self):
		return self.rotation

	def toSerializible(self):
		return {"position":self.position, "rotation":self.rotation}
