from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from panda3d.core import OrthographicLens


configVars = """
win-size 1280 720
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0.1, 0.1, 0.1, 1)
        self.cam.setPos(0, -5, 0)

        self.cube1 = self.loader.loadModel("models/box")
        self.cube1.setPos(1, 0, 0)
        self.cube1.setScale(50)
        self.cube1.reparentTo(self.render)

        self.cube2 = self.loader.loadModel("models/box")
        self.cube2.setPos(-70, 8, 0)
        self.cube2.setScale(50)
        self.cube2.reparentTo(self.render)

        lens = OrthographicLens()
        lens.setFilmSize(1280, 720)
        lens.setNearFar(-50, 50)
        self.cam.node().setLens(lens)


game = MyGame()
game.run()
