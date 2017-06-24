#!/usr/bin/env/ python3
from fishcodeServer import Map

class Server(object):

	def __init__(self):
		self.maps = []

	def newMap(self, area):
		myMap = Map(area)
		self.maps.append(myMap)

	def getMaps(self):
		return self.maps

	def playerJoin(self, myMap, player):
		myMap.addPlayer(player)

	def playerLeave(self, player):
		player.getMap.removePlayer()

	def tick(self):
		#run player update method
		pass
