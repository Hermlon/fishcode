#!/usr/bin/env/ python3
import random, json

class Map(object):

	def __init__(self, area):
		self.area = area
		self.entities = []
		self.maptime = 0

	def tick(self):
		self.maptime += 1
		print(self.maptime)
		for entity in self.entities:
			entity.update()

	def addPlayer(self, player, pos=None):
		if not pos:
			pos = self.randPos(player)
		player.setMap(self)
		player.getLocation().setPosition(pos)
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
		half = entity.getSize() / 2
		xPos = random.randint(half, self.area[0] - half)
		yPos = random.randint(half, self.area[1] - half)
		return (xPos, yPos)

	def toJSON(self):
		#import pdb; pdb.set_trace()
		return json.dumps(self.toSerializible())

	def toSerializible(self):
		def doSerializible(s):
			return s.toSerializible()
		e = list(map(doSerializible, self.entities))
		return {"area":self.area, "entities":e}
