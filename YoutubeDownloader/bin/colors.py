class Colors:
    DARK  = "#1C1C1C"
    LIGHT = "#939FAB"
    GREY  = "#45494A"
    BLUE  = "#3D59AB"
    RED   = "#A52A2A"

    def __init__(self):
        self.currentColor = []
        self.currentColor.append(self.DARK)
        self.currentColor.append(self.LIGHT)
        self.currentColor.append(self.GREY)
        self.currentColor.append(self.BLUE)
        self.currentColor.append(self.RED)
        self.DarkLightMode()

    def GetCurrentColor(self):
        return self.currentColor

    def DarkLightMode(self):
        self.currentColor[0] = self.ReverseColor(self.currentColor[0])
        self.currentColor[1] = self.ReverseColor(self.currentColor[1])

    def ReverseColor(self, color):
        reverseColor = "#"
        for chrHex in range(1, len(color), 2):
            reverseColor += hex(255 - int(color[chrHex:chrHex + 2], 16))[2:]
        return reverseColor

