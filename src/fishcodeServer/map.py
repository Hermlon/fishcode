#!/usr/bin/env/ python3
class Map(object):
	
	def __init__(self, area):
		self.area = area
		self.players = []
		
	def addPlayer(self, player):
		self.player.setMap(self)
		self.players.append(player)
		
	def removePlayer(self, player):
		self.players.setMap(None)
		self.players.remove(player)
		
	def updatePosition(self, player, position):
		self.players[player] = position
		
	def getPostion(self, player):
		return self.players[player]
		
	def updateShot(self):
		pass
