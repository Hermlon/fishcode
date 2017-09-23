#!/usr/bin/env/ python3
from fishcodeServer.server import Server
from fishcodeServer.player import Player
import math
#from threading import Thread
myServer = Server()
myServer.newMap((400, 300))
myMap = myServer.getMaps()[0]
player1 = Player("player1", 50)
player1.setVelocity(0)
player1.getLocation().setPosition((10, 10))
player2 = Player("player2", 50)
myServer.playerJoin(myMap, player1)
myServer.playerJoin(myMap, player2)
player2.getLocation().setPosition((30, 10))
player2.getLocation().setRotation(math.pi / 2)
#myMap.addPlayer(player1, (20,20))
#myMap.addPlayer(player2, (20,120))

#player1.setCode("""
#rotation = 3
#shoot = True
#playerdecision = PlayerDecision(rotation, shoot)""")

myServer.start()
#print(myMap.toJSON())
