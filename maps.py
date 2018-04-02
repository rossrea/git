import random

class Map(object):
    _Map=[]
    _X=0
    _Y=0
    _CurrentTile=[]
    _StartingTile=[]
    
    def __init__(self, mymap, x, y):
        self._Map=mymap
        self._X=x
        self._Y=y
        #try:
        _StartingTile=mymap[0][random.randint(0,y-1)]
        _CurrentTile=_StartingTile
        #except:
        #    print("Error: Unable to assign the starting tile.")

    def GetCurrentTile(self):
        return self._Description

    def SetDescription(self, description):
        self._Description=description

    def GetEvent(self):
        return self._Event
        
    def GetTileType(self):
        return self._TileType

    def GetItem(self):
        return self._Item

    def SetItem(self, item):
        self._Item=item

    def DisplayTile(self):
        print("Description => '{}'".format(self._Description))
        print("TileType => '{}'".format(self._TileType))
        print("Event => '{}'".format(self._Event))
        print("Item => '{}'".format(self._Item))
