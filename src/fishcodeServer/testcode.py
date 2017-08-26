#!/usr/bin/env/ python3
from fishcodeServer.location import Location
from fishcodeServer.playerdecision import PlayerDecision
from fishcodeServer.code import Code

class TestCode(Code):

    def update(self, playername, data):
        rotation = 1
        shoot = False
        return PlayerDecision(rotation, shoot)
