#!/usr/bin/env/ python3
class Map(object):
	
	def __init__(self, area):
		self.area = area
		self.players = {}
		
	def addPlayer(self, player, pos=None):
		player.setMap(self)
		if not pos:
			pos = self.randPos(player)
		player.setPosition(pos)
		print(pos)
		self.players[player] = pos
		
	def removePlayer(self, player):
		self.players.setMap(None)
		del self.players[player]
		
	def updatePosition(self, player, position):
		self.players[player] = position
		
	def getPostion(self, player):
		return self.players[player]
		
	def updateShot(self):
		pass

	def randPos(self, player):
		return (20, 20)
