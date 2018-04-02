class Tile(object):
    _Description=""
    _TileType=""
    _Event=""
    _Item=""
    
    def __init__(self, description, tiletype, event, item):
        self._Description=description
        self._TileType=tiletype
        self._Event=event
        self._Item=item

    def GetDescription(self):
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
    


    
