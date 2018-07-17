import HaqPyTools.UI


class Machine:

    def __init__(self, name="", color="RED"):
        self.name = name
        self.color = color

    def getName(self):
        return self.name

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def __str__(self):
        info = "MACHINE NAME: " + self.name + "\n"
        info = info + "COLOR: " + self.color + "\n"

        return info
