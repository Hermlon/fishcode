#!/usr/bin/env/ python3
class Player(object):
	
	def __init__(self, name):
		self.name = name
		self.shots = []
		
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

	def getEnergy(self):
		return self.energy
		
	def shoot(self):
		shootLoseEnergy()
		newShot = Shot(self)
		newShot.setPosition(self.getPosition())
		newShot.setRotaion(self.getRotation())
		self.shots.append()
		self.myMap.updateShot()
		
	def removeShot(self, shot):
		self.shots.remove(shot)
		
	def getShots(self):
		return self.shots

	def shootLoseEnergy(self):
		self.setEnergy(self.getEnergy - 1)
		
	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code
		
	def getName(self):
		return self.name
		
	def setMap(self, myMap):
		self.myMap = myMap
		
	def getMap(self):
		return self.myMap
		
	def getSize(self):
		return self.size
		
	def setSize(self, size):
		self.size = size
		
	def objectHitsPlayer(self, objectPos):
		if((objectPos[0] >= self.getPosition()[0] - self.getSize()[0] / 2) and (objectPos[0] <= self.getPosition[0] + self.getSize()[0] / 2)
		and (objectPos[1] >= self.getPosition()[1] - self.getSize()[1] / 2) and (objectPos[1] <= self.getPosition[1] + self.getSize()[1] / 2)):
			return True
		return False
