#!/usr/bin/env/ python3
from fishcodeServer.entity import Entity

class Shot(Entity):

	shotsize = 40

	def __init__(self, player):
		super().__init__(self.shotsize)
		self.player = player
		self.setVelocity(1)

	def getPlayer(self):
		return self.player

	def toSerializible(self):
		d = super().toSerializible()
		d.update({"shotsize":self.getSize()})
		return d
