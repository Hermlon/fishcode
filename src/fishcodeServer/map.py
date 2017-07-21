#!/usr/bin/env/ python3
import random

class Map(object):

	def __init__(self, area):
		self.area = area
		self.entities = []
		self.maptime = 0

	def tick():
		self.maptime += 1

	def addPlayer(self, player, pos=None):
		if not pos:
			pos = self.randPos(player)
		player.setMap(self)
		player.setPosition(pos)
		self.entities.append(player)

	def removePlayer(self, player):
		self.players.setMap(None)
		del self.players[player]

	def updatePosition(self, player, position):
		self.players[player] = position


	def getPosition(self, player):
		return self.players[player]

	def updateShot(self):
		pass

	def randPos(self, entity):
		halfx = entity.getSize[0] / 2
		halfy = entity.getSize[1] / 2
		xPos = random.randint(halfx, self.area.getSize()[0] - halfx)
		yPos = random.randint(halfy, self.area.getSize()[1] - halfy)
		return (xPos, yPos)
