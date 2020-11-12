from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData


configVars = """
win-size 1280 720
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)

"""
command i used in the video:
egg-texture-cards -o Jack.egg -fps 10 Walk1.png Walk2.png Walk3.png Walk4.png Walk5.png Walk6.png Walk7.png Walk8.png Walk9.png Walk10.png
"""


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0.1, 0.1, 0.1, 1)
        self.cam.setPos(0, -5, 0)

        self.jack = self.loader.loadModel("assets/texture_cards/Jack")
        self.jack.reparentTo(self.render)


game = MyGame()
game.run()
