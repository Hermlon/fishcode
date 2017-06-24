#!/usr/bin/env/ python3
class Shot(object):
	
	def __init__(self, player):
		self.player = player
		
	def setPosition(self, player, position):
		self.players[player] = position
		
	def getPostion(self, player):
		return self.players[player]
		
	def getPlayer(self):
		return self.player
