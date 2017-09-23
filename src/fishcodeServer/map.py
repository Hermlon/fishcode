#!/usr/bin/env/ python3
import random, json, math

class Map(object):

	def __init__(self, area):
		self.area = area
		self.players = []
		self.maptime = 0

	def tick(self):
		self.maptime += 1

		#This is a test
		if self.maptime == 4:
			self.players[0].shoot()


		print(self.maptime)
		for player in self.players:
			player.update()
			self.updatePosition(player)
			print(player.getName() + ": " + str(player.getLocation().getPosition()))
		for player in self.players:
			self.updateShots(player)

	def addPlayer(self, player, pos=None):
		if not pos:
			pos = self.randPos(player)
		player.setMap(self)
		player.getLocation().setPosition(pos)
		self.players.append(player)

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
		else:
			return False
		return True

	def updateShots(self, player):
		print("Shots of " + player.getName())
		for shot in player.getShots():
			print("x: " + str(shot.getLocation().getPosition()))
			if self.updatePosition(shot):
				for p in self.players:
					if shot.hitsEntity(p):
						p.shootLoseEnergy()
			else:
				player.removeShot(shot)

	def getPosition(self, player):
		return self.players[player]

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
		e = list(map(doSerializible, self.players))
		return {"area":self.area, "players":e}
