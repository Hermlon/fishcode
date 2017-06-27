#!/usr/bin/env/ python3
import random

class Map(object):

	def __init__(self, area):
		self.area = area
		self.players = {}

	def addPlayer(self, player, pos=None):
		if not pos:
			pos = self.randPos(player)
		player.setMap(self)
		player.setPosition(pos)

	def removePlayer(self, player):
		self.players.setMap(None)
		del self.players[player]

	def updatePosition(self, player, position):
		self.players[player] = position


	def getPosition(self, player):
		return self.players[player]

	def updateShot(self):
		pass

	def randPos(self, player):
		xPos = random.randint(20, 380)
		yPos = random.randint(20, 280)
		
		return(xPos, yPos)
