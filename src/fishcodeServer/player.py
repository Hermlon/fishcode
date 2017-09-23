#!/usr/bin/env/ python3
from fishcodeServer.entity import Entity
from fishcodeServer.code import Code
from fishcodeServer.shot import Shot

class Player(Entity):

	def __init__(self, name, size):
		super().__init__(size)
		self.name = name
		self.shots = []
		self.energy = 10
		#self.texture.generateDefaultImg()
		self.code = "playerdecision =  PlayerDecison(4, False)"

	def update(self):
		decision = Code.update(self.code, self.name, self.getMap().toJSON())
		print(decision.getRotation())
		print(decision.isShoot())
		self.getLocation().setRotation(decision.getRotation())
		if decision.isShoot():
			self.shoot()

	def setEnergy(self, energy):
		self.energy = energy

	def getEnergy(self):
		return self.energy

	def shoot(self):
		self.shootLoseEnergy()
		newShot = Shot(self)
		newShot.setMap(self.getMap())
		newShot.getLocation().setPosition(self.getLocation().getPosition())
		newShot.getLocation().setRotation(self.getLocation().getRotation())
		self.shots.append(newShot)

	def removeShot(self, shot):
		self.shots.remove(shot)

	def getShots(self):
		return self.shots

	def shootLoseEnergy(self):
		self.setEnergy(self.getEnergy() - 1)
		print("Player " + self.getName() + " shooted.")

	def shootedLoseEnergy(self):
		self.setEnergy(self.getEnergy() - 1)
		print("Player " + self.getName() + " was shot.")

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def getName(self):
		return self.name

	def toSerializible(self):
		d = super().toSerializible()
		def doSerializible(s):
			return s.toSerializible()
		shots = list(map(doSerializible, self.shots))
		d.update({"name":self.name, "shots":shots})
		return d
