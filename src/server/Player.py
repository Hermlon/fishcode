#!/usr/bin/env/ python3
class Player(object):
	
	def __init__(self, myMap, name):
		self.name = name
		self.myMap = myMap
		
	def setPosition(self, position):
		self.myMap.updatePosition(self, position)
		 
	def getPosition(self):
		return self.myMap.getPosition(self)
			
	def setRotation(self, rotation):
		self.rotation = rotation
		
	def getRotation(self):
		return self.rotation
		
	def setEnergy(self, energy):
		self.energy = energy
