import tiles as Tiles
import random
import sys
import signal


#ToDo:
#Map Class (include starting tile, available items?, movement)
#MapObject Generator
#MapGenerator(x,y,List of MandatoryObjects,List of FillerObjects,Listofitemstofind)
#Leader board (in file?)  #of Turns, # of items found show top turns, show top items found?
#Welcome()
#CheckWatch() Print the time, but add a minute
#BuildMandatoryTiles for Scenario River, Bay, Gulf, etc ...
#BuildOptional(filler)Tiles for Scenario River, Bay, Gulf, etc ...
#Build master list of items
#Spread items out over scenario tiles
#Keep an inventory list
#Allow user to see items they can find "Bent fishing hook" might lead someone to go back into the bay until it is found?
#Movement in scenarios (one per scenario or can it be generic enough?)
#Graphics?/Images?
#Replace raw_input with a getch function?

#Ideas:
#Keep track of moves or time
#Search area adds to moves? ("time to find as attribute?") If search<Timetofind then missed it, but time added to moves
#Let person "move around" without going to a map.  Soon as they got to the "scenario intro spot" go to map for that scenario.
#Allow areas to be reentered
#In the scenario "maps" have unrestricted movement (i.e. full grid available)  (Easier to start)
#If we do time, need to "get back to the dorm" by time X?
#If late?
#In the free move area, allow for "G"o to Outdoor Rec, take boat to "R"iver, "B"ay,"G"ulf,(can add more as time permits.
#Which ever area they pick, go to that "map" and do "scenario loop" until the leave, die, throwout, caught busting phase
#Scenario vehicles affect the time and depending on the tiles, could "end quickly" Jon Boat in ocean as a storm tile is entered
#Allow user to go to non=map areas?  (like a night club?)  (time wasters
#Allow them to "Check their watch" or "Search" almost anywhere?

def signal_handler(signal, frame):
    print("ctrl-c pressed ... exitting.")
    sys.exit(0)

def GenerateMap(Len,Width,MandatoryTiles,FluffTiles,AvailableItems):
    Map=[]
    MyTile=Tiles.Tile
    for x in range(Len):
        MapRow=[]
        for y in range(Width):
            i=random.randint(0,len(FluffTiles)-1)
            MapRow.append(FluffTiles[i])
        Map.append(MapRow)

    for i in range(len(MandatoryTiles)):
        x=random.randint(0,Len-1)
        y=random.randint(0,Width-1)
        while True:
            if Map[x][y] in FluffTiles:
                MyTile=MandatoryTiles[i]
                print("Replacing fluff tile with".format(MyTile.GetDescription()))
                break
            else:
                x=random.randint(0,Len-1)
                y=random.randint(0,Width-1)
                

    for x in range(Len):
        for y in range(Width):
            MyTile=Map[x][y]
            print("Tile at {},{} (X,Y) is:".format(x,y))
            MyTile.DisplayTile()

    return Map
    
def BayScenario():
    print("**** Bay code goes here.")
    return False

def GulfScenario():
    print("**** Gulf code goes here.")
    return True

def RiverScenario():

    print("**** River code goes here.")

    global TimeSpent
    global Inventory
    DynamiteCounter=0
    DisplayEvent=False
    EventText=""

    CurrentTile=Map[0][0]
    print("\nYou decide to take a trip down the river.  A storm is on the horizon, but is 'supposed' to clear soon.\n")
    print("blah,blah ... (storyline) ...\n\n")

    while True:
        #ToDo: Check the time versus curfew.  Busted?
        if DynamiteCounter>0:
            DynamiteCounter -=1
            if DynamiteCounter==0:
                print("*****************************")
                print("*****************************")
                print("******BOOOOOOOOMMMMMM!!******")
                print("*****************************")
                print("*****************************")
                print("\nWith a loud cackle you hear, 'Dats what I call fishing!!!!!!'")
        print("******\nYou see {}.\n".format(CurrentTile.GetDescription()))
        if DisplayEvent:
            print EventText
            DisplayEvent=False
        print("(I)nventory, (L)ook around, (F)ish, (C)heck watch, move (N)orth, (S)outh, (E)ast or (W)est, e(X)it")
        UserSelection=raw_input("What would you like to do next?: ").upper()
        if UserSelection=="X":
            #ToDo: Check if they are at the dock, if now, print a message saying they take X times the number of spaces to get back?
            #Without a map, we will assume they are not at the dock...
            print("You return to the dock and are safely back on shore.\n")
            return True
        elif UserSelection=="I":
            if len(Inventory)==0:
                print("You have nothing in your inventory.")
            else:
                print("You are currently holding:\n {}".format(Inventory))
        elif UserSelection=="L":
            UserSelection=int(raw_input("How many minutes would you like to search the area? "))
            if UserSelection==0:
                print("You decide not to spend time searching the current location.")
            else:
                TimeSpent+=UserSelection
                if (len(CurrentTile.GetItem()) == 0) or UserSelection<random.randint(5,10):
                    print("You spend {} minutes searching the area and find nothing.".format(UserSelection))
                else:
                    Inventory.append(CurrentTile.GetItem())
                    print("You spend {} minutes searching the area and find {}.".format(UserSelection,CurrentTile.GetItem()))
                    CurrentTile.SetItem("")
                    if CurrentTile.GetEvent()=="Snake":
                        if Inventory.count("fishing net")==1:
                            print("You capture the snake with your fishing net.")
                            CurrentTile.SetDescription("baby snakes in the water looking for their mother")
                        else:
                            #Make it random to see if the get bit?   For now ... BITE EM! =)
                            print("Without a net, you get bit by the snake and need to go to the hospital!")
                            return False                            
                    elif CurrentTile.GetEvent()=="Net":
                        CurrentTile.SetDescription("water with a surface not as shiny as earlier")
        elif UserSelection=="F":
            UserSelection=int(raw_input("How many minutes would you like to stay and fish? "))
            if UserSelection==0:
                print("You decide not skip fishing for now.")
            else:
                TimeSpent+=UserSelection
        elif UserSelection=="C":
            CheckWatch()
        elif UserSelection in ["N","S","E","W"]:
            #ToDo: Check Boundary
            #If you can move, add time and move
            #If not print message and continue to loop (don't add time)

            #No map so randomize what happens:
            
            WingIt=random.randint(1,7)
            if WingIt==1:
                #boundary
                print("The bank of the river is too rough to traverse in that direction.")
            elif WingIt<4:
                #Mandatory tile
                TimeSpent+=3
                CurrentTile=RiverTiles[random.randint(0,len(RiverTiles)-1)]
                #ToDo: Check for special events
                if CurrentTile.GetEvent()=="Fisherman":
                    DisplayEvent=True
                    EventText="She says, 'You better have the right bait if you want to catch fish in this river!'\n"
                    DynamiteCounter=random.randint(3,10)
            else:
                #random tile
                TimeSpent+=3
                CurrentTile=RiverFluffTiles[random.randint(0,len(RiverFluffTiles)-1)]
        else:
            print("'{}' is an invalid selection.".format(UserSelection))
            
                      
def Welcome():
    print("**** Welcome Information code goes here.\n\n")

def CheckWatch():
    global TimeSpent
    TimeSpent+=1
    print TimeSpent

def DisplayLeaderBoard():
    print("**** Leader Board Code")


#Start Real Program
#Tempcode Start
Len=0
Width=0
#Tempcode End    

signal.signal(signal.SIGINT, signal_handler)

RiverTiles=[]
RiverFluffTiles=[]
RiverTiles.append(Tiles.Tile("a pool of floating fish",1,"","a nearly-dead fish"))
RiverTiles.append(Tiles.Tile("someone fishing in a boat",1,"Fisherman",""))
RiverTiles.append(Tiles.Tile("river Tile 2",1,"",""))
RiverTiles.append(Tiles.Tile("a snake in the water",1,"Snake","a dead snake"))
RiverTiles.append(Tiles.Tile("water with a shiny surface",1,"Net","fishing net"))
RiverTiles.append(Tiles.Tile("river Tile 4",1,"","old lure"))
RiverTiles.append(Tiles.Tile("river Tile 5",1,"","torn shirt")) 
RiverFluffTiles.append(Tiles.Tile("clear, open water",0,"",""))
RiverFluffTiles.append(Tiles.Tile("blue water",0,"","flotsam"))
RiverFluffTiles.append(Tiles.Tile("beautiful, blue water",0,"",""))
RiverFluffTiles.append(Tiles.Tile("slightly, murky water",0,"","a broken board"))

    
TimeSpent=0             #Time (or turns?) spent in the game.  Use in the leader board results
Map=[]
RiverMap=[]
BayMap=[]
GulfMap=[]
#RiverTiles=[]
BayTiles=[]
GulfTiles=[]
#RiverFluffTiles=[]
BayFluffTiles=[]
GulfFluffTiles=[]
Inventory=[]
#Available items format: item, boolean to indicate if it has been placed in a scenario.
AvailableItems=[["Gold Coin",False],
                ["Fishing Hook",False],
                ["Wrench",False]]


RiverMap=GenerateMap(5,5,RiverTiles,RiverFluffTiles,AvailableItems)
#BayMap=GenerateMap(Len,Width,BayTiles,BayFluffTiles,AvailableItems)
#GulfMap=GenerateMap(Len,Width,GulfTiles,GulfFluffTiles,AvailableItems)
Welcome()

StillPlaying=True

while(StillPlaying):
    #All "scenario" adventures must return a "StillPlaying" result.  i.e. If they drowned in the ocean, the BayCode would return False (no longer playing)
    if TimeSpent>600:  #10 hours hardcoded
        print("You lose track of time and bust curfew!")
        break
    print("blah, blah (storyline) ... \n")
    print("(R)iver (B)ay (G)ulf (X)bar (Q)uit")
    UserSelection=raw_input("What would you like to do next? ").upper()
    if UserSelection == "B":
        StillPlaying=BayScenario()
    elif UserSelection == "G":
        StillPlaying=GulfScenario()
    elif UserSelection == "R":
        StillPlaying=RiverScenario()        
    elif UserSelection == "X":
        TimeWaster=raw_input("How many drinks would you like to have at Billy Bob's Bangin Bar? ")
        TimeWaster=int(TimeWaster)
        if TimeWaster==0:
            print("Probably a good idea.\nYou leave the bar.")
        elif TimeWaster==1:
            print("After a quick drink, you leave the bar for more adventures!")
        elif TimeWaster<3:
            print("You spend a good amount of time at the bar, but decide to leave, finding nothing more than a slight headache.")
        else:
            StillPlaying=False
            print("You lose track of time and bust curfew!")
    elif UserSelection == "Q":
        sys.exit(0)
    else:
        print("That option isn't availabe ... yet!\n")

DisplayLeaderBoard()

'''
li=[1,2,3,4,5]
f=list(map(lambda x:x*2,li))
print f
'''
