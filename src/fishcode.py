#!/usr/bin/env/ python3
from fishcodeServer.server import Server
from fishcodeServer.player import Player
#from threading import Thread
myServer = Server()
myServer.newMap((400, 300))
myMap = myServer.getMaps()[0]
player1 = Player("player1", (50,50))
player2 = Player("player2", (50,50))
myServer.playerJoin(myMap, player1)
myServer.playerJoin(myMap, player2)



player1.setCode("""
from fishcodeServer.location import Location
from fishcodeServer.playerdecision import PlayerDecision
from fishcodeServer.code import Code

class MyCode(Code):

    def update(self, playername, data):
        rotation = 3
        import pdb; pdb.set_trace()
        shoot = True
        return PlayerDecision(rotation, shoot)
        """, "MyCode")

myServer.start()
#print(myMap.toJSON())

"""print("test")
player1.setPosition((39,39))
print(player1.getPosition())
player1.setSize((20,20))
print(player1.objectHitsPlayer((50,50)))"""

#myPlayer = Player("test", (50,50))
