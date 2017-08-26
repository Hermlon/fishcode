#!/usr/bin/env/ python3
from fishcodeServer.map import Map
import time

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
		for mymap in self.maps:
			mymap.tick()

	def start(self):
		while True:
			self.tick()
			time.sleep(1)
