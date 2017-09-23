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
			self.updatePosition(entity)

	def addPlayer(self, player, pos=None):
		if not pos:
			pos = self.randPos(player)
		player.setMap(self)
		player.getLocation().setPosition(pos)
		self.entities.append(player)

	def removePlayer(self, player):
		self.players.setMap(None)
		del self.players[player]

	def updatePosition(self, entity):
		yAdd = math.sin(entity.getLocation().getRotation()) * entity.getVelocity()
		xAdd = math.cos(entity.getLocation().getRotation()) * entity.getVelocity()
		xNew = entity.getLocation().getX() + xAdd
		yNew = entity.getLocation().getY() + yAdd
		if xNew <= entity.getMap().getArea()[0] and xNew >= 0 and yNew <= entity.getMap().getArea()[1] and yNew >= 0:
			entity.getLocation().setPosition((xNew, yNew))
		print("---------")
		print(str(xAdd) + "|" + str(yAdd))
		print(entity.getLocation().getPosition())
		print("---------")

	def getPosition(self, player):
		return self.players[player]

	def updateShot(self):
		pass

	def randPos(self, entity):
		half = entity.getSize() / 2
		xPos = random.randint(half, self.area[0] - half)
		yPos = random.randint(half, self.area[1] - half)
		return (xPos, yPos)

	def getArea(self):
		return self.area

	def toJSON(self):
		#import pdb; pdb.set_trace()
		return json.dumps(self.toSerializible())

	def toSerializible(self):
		def doSerializible(s):
			return s.toSerializible()
		e = list(map(doSerializible, self.entities))
		return {"area":self.area, "entities":e}
