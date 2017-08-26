#!/usr/bin/env/ python3

class PlayerDecision(object):

    def __init__(self, rotation, shoot):
        self.rotation = rotation
        self.shoot = shoot

    def getRotation(self):
        return self.rotation

    def setRotation(self, rotation):
        self.rotation = rotation

    def isShoot(self):
        return self.shoot

    def setShoot(self, location):
        self.shoot = shoot
