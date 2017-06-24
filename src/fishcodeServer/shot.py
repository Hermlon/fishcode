#!/usr/bin/env/ python3
class Shot(object):
	
	def __init__(self, player):
		self.player = player
		
	def setPosition(self, position):
		self.position = position
		
	def getPostion(self):
		return self.position
		
	def setRotation(self, rotation):
		self.rotation = rotation
		
	def getRotation(self):
		return rotation
		
	def getPlayer(self):
		return self.player
