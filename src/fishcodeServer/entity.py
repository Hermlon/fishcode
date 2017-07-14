#!/usr/bin/env/ python3
import location

class Entity(object):
	def __init__(self, size):
		self.myMap = None
		self.location = Location()
		self.size = size

	def setLocation(self, location):
		self.location = location

	def getLocation(self):
		return self.location

	def setPosition(self, position):
		self.location.setPosition(position)

	def getPosition(self):
		return self.location.getPosition

	def setRotation(self, rotation):
		self.location.setRotation(rotation)

	def getRotation(self):
		return self.location.getRotation()

	#Defined in units per tick, unit is defined by the size of the area and tick is always one, no matter how much real time passed
	def setSpeed(self, speed):
		self.speed = speed

	def getSpeed(self):
		return self.speed

	def setMap(self, myMap):
		self.myMap = myMap

	def getMap(self):
		return self.myMap

	def getSize(self):
		return self.size

	def setSize(self, size):
		self.size = size

	def objectHitsPlayer(self, objectPos):
		if((objectPos[0] >= self.getPosition()[0] - self.getSize()[0] / 2)
		and (objectPos[0] <= self.getPosition()[0] + self.getSize()[0] / 2)
		and (objectPos[1] >= self.getPosition()[1] - self.getSize()[1] / 2)
		and (objectPos[1] <= self.getPosition()[1] + self.getSize()[1] / 2)):
			return True
		return False