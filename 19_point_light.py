from panda3d.core import loadPrcFileData

configVars = """
win-size 1280 720
fullscreen 0
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)

from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight
from math import sin, cos


class SimplePointLight(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0, 1)
        self.tree = self.loader.loadModel('my-models/christmas_tree')
        self.tree.setPos(0, 0, -2.5)
        self.tree.reparentTo(self.render)

        self.light_model = self.loader.loadModel('models/misc/sphere')
        self.light_model.setScale(0.2, 0.2, 0.2)
        self.light_model.reparentTo(self.render)

        self.cam.setPos(0, -12, 0)

        self.lightX = 0
        self.lightSpeed = 1

        plight = PointLight("plight")
        plight.setColor((1,1,1,1))
        self.plnp = self.render.attachNewNode(plight)
        # plight.setAttenuation((0, 0, 1))
        self.render.setLight(self.plnp)

        self.taskMgr.add(self.move_light, "move-light")

    def move_light(self, task):
        dt = globalClock.getDt()

        self.plnp.setPos(cos(self.lightX)*4, sin(self.lightX)*4, 0)
        self.light_model.setPos(self.plnp.getPos())
        self.lightX += self.lightSpeed * dt

        return task.cont


game = SimplePointLight()
game.run()