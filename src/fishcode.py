#!/usr/bin/env/ python3
from fishcodeServer import Server, Player
#/home/hermlon/code/projects/fishcode/src/fishcodeServer/server.py
myServer = Server()
myServer.newMap((400, 300))
myMap = myServer.getMaps()[0]
player1 = Player("player1")
player2 = Player("player2")
myServer.playerJoin(myMap, player1)
myServer.playerJoin(myMap, player2)
