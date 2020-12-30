from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, PointLight, AmbientLight
import math


configVars = """
win-size 1280 720
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0, 1)
        self.cam.setPos(0, -20, 5)

        self.plane = self.loader.loadModel('my-models/planeTB')
        self.plane.setPos(-5, 5, 0)
        self.plane.reparentTo(self.render)

        self.sphere = self.loader.loadModel("my-models/icosphere")
        self.sphere.reparentTo(self.render)

        alight = AmbientLight('alight')
        alight.setColor((0.2, 0.2, 0.2, 1))
        alnp = self.render.attachNewNode(alight)
        self.plane.setLight(alnp)

        plight = PointLight('plight')
        plight.setColor((1, 1, 1, 1))
        plnp = self.sphere.attachNewNode(plight)
        self.plane.setLight(plnp)

        self.render.setShaderAuto()

        self.taskMgr.add(self.move_light, "move-light")

    def move_light(self, task):
        ft = globalClock.getFrameTime()

        self.sphere.setPos(math.sin(ft) * 10, 0, 5)

        return task.cont


game = MyGame()
game.run()
