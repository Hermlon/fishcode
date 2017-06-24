#!/usr/bin/env/ python3
class Map(object):
	
	def __init__(self, area):
		self.area = area
		
		
	def updatePosition(self, player, position):
		self.players[player] = position
		
	def getPostion(self, player):
		return self.players[player]
		
	def updateShot(self, shot):
		
