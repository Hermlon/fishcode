#!/usr/bin/env/ python3
from fishcodeServer.location import Location
from fishcodeServer.texture import Texture
from fishcodeServer.serializable_mixin import SerializableMixin
import math

class Entity(SerializableMixin):
	def __init__(self, size):
		self.myMap = None
		self.location = Location()
		self.size = size
		self.setVelocity(0)
		#self.texture = Texture(self.getSize())

	def update(self):
		yAdd = math.sin(self.getLocation().getRotation()) * self.getVelocity()
		xAdd = math.cos(self.getLocation().getRotation()) * self.getVelocity()
		xNew = self.getLocation().getX() + xAdd
		yNew = self.getLocation().getY() + yAdd
		self.getLocation().setPosition((xNew, yNew))
		print("---------")
		print(str(xAdd) + "|" + str(yAdd))
		print(self.getLocation().getPosition())
		print("---------")

	def setLocation(self, location):
		self.location = location

	def getLocation(self):
		return self.location

	#Defined in units per tick, unit is defined by the size of the area and tick is always one, no matter how much real time passed
	def setVelocity(self, velocity):
		self.velocity = velocity

	def getVelocity(self):
		return self.velocity

	def setMap(self, myMap):
		self.myMap = myMap

	def getMap(self):
		return self.myMap

	def getSize(self):
		return self.size

	def setSize(self, size):
		self.size = size

	def getTexture(self):
		return self.texture

	def setTexture(self, texture):
		self.texture = texture

	def hitsEntity(self, otherEntity):
		radiusSum = self.getSize() + otherEntity.getSize()
		deltax = abs(self.getLocation().getX() - otherEntity.getLocation().getX())
		deltay = abs(self.getLocation().getY() - otherEntity.getLocation().getY())
		distance = math.sqrt(deltax ** 2 + deltay ** 2)
		return distance <= radiusSum

	def toSerializible(self):
		#return {"location":self.location.toSerializible(), "size":self.size, "texture":self.texture.toSerializible()}
		return {"location":self.location.toSerializible(), "size":self.size, "velocity":self.velocity}
