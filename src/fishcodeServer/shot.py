#!/usr/bin/env/ python3
import entity

class Shot(Entity):

	shotsize = (2, 5)

	def __init__(self, player):
		super().__init__(shotsize)
		self.player = player

	def getPlayer(self):
		return self.player

	def toSerializible(self):
		d = super().toSerializible()
		d.update({"shotsize":shotsize})
		return d
