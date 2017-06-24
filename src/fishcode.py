#!/usr/bin/env/ python3
from fishcodeServer import Server, Player
#from threading import Thread
myServer = Server()
myServer.newMap((400, 300))
myMap = myServer.getMaps()[0]
player1 = Player("player1")
player2 = Player("player2")
myServer.playerJoin(myMap, player1)
myServer.playerJoin(myMap, player2)

print("test")
player1.setPosition((39,39))
print(player1.getPosition())
player1.setSize((20,20))
print(player1.objectHitsPlayer((50,50)))
