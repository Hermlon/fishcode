#!/usr/bin/env/ python3
from fishcodeServer.playerdecision import PlayerDecision

class Code(object):

    @staticmethod
    def update(code, playername, data):
        playerdecision = None
        exec(code)
        return playerdecision
