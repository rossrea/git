import random
import sys

class Map(object):
    _Map=[]
    _MaxX=0
    _MaxY=0
    _X=0
    _Y=0
    _CurrentTile=[]
    _StartingTile=[]
    _BoundaryMsg=""
    
    def __init__(self, mymap, x, y, boundary_msg, starting_tile_x=-1, starting_tile_y=-1):
        self._Map=mymap
        self._MaxX=x-1  #Make it zero-based
        self._MaxY=y-1  #Make it zero-based
        self._BoundaryMsg=boundary_msg
        #try:

        if starting_tile_x==-1:     #If 'x' is defaulted, y has to be too <Python>
            self._X=random.randint(0,x-1)
            self._Y=random.randint(0,y-1)
        elif starting_tile_==-1:    #Looks like only y is defaulted
            self._X=starting_tile_x
            self._Y=random.randint(0,y-1)
        else:
            self._X=starting_tile_x
            self._Y=starting_tile_y
        self._StartingTile=mymap[self._X][self._Y]
        self._CurrentTile=self._StartingTile
        #except:
        #    print("Error: Unable to assign the starting tile.")

    def GetCurrentTile(self):
        return self._CurrentTile

    def GetLocation(self):
        return self._X,self.Y

    def GetStartingTile(self, description):
        return self._StartingTile

    def Move(self,direction):
        direction=direction.upper()
        if direction not in ["N","S","E","W"]:
            print("Error: valid directions are (N,S,E,W)")
            sys.exit(1)
        if direction=="N":
            self.MoveNorth()
        elif direction=="S":
            self.MoveSouth()
        elif direction=="E":
            self.MoveEast()
        else:
            self.MoveWest()
        self._CurrentTile=self._Map[self._X][self._Y]
        return self._CurrentTile
        
    def MoveNorth(self):
        print"North"
        if self._Y==self._MaxY:
            print self._BoundaryMsg
        else:
            self._Y+=1

    def MoveSouth(self):
        print"South"
        if self._Y==0:
            print self._BoundaryMsg
        else:
            self._Y-=1

    def MoveEast(self):
        print"East"
        if self._X==self._MaxX:
            print self._BoundaryMsg
        else:
            self._X+=1

    def MoveWest(self):
        print"West"
        if self._X==0:
            print self._BoundaryMsg
        else:
            self._X-=1
            
    def DisplayMap(self):
        print("Size of map is {},{}.".format(self._MaxX+1,self._MaxY+1))    #Shifting it to one-based for humans! =)
        print("Current location on the map is {},{}.".format(self._X,self._Y))
        print("Boundary message is: '{}'.".format(self._BoundaryMsg))


