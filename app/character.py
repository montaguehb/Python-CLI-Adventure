class Character():
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        pass