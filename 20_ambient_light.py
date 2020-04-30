from panda3d.core import loadPrcFileData

configVars = """
win-size 1280 720
fullscreen 0
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)

from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight, AmbientLight
from math import sin, cos


class PointAndAmbientLight(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0, 1)
        self.cam.setPos(0, -12, 0)

        self.tree = self.loader.loadModel('my-models/christmas_tree')
        self.tree.setPos(0, 0, -2.5)
        self.tree.reparentTo(self.render)

        self.light_model = self.loader.loadModel('models/misc/sphere')
        self.light_model.setScale(0.2, 0.2, 0.2)
        self.light_model.setPos(4, 0, 0)
        self.light_model.reparentTo(self.render)

        plight = PointLight("plight")
        plight.setColor((1,1,1,1))
        self.plnp = self.light_model.attachNewNode(plight)
        # plight.setAttenuation((0, 0, 1))
        self.tree.setLight(self.plnp)

        alight = AmbientLight("alight")
        alight.setColor((0.04, 0.04, 0.04, 1))
        alnp = self.render.attachNewNode(alight)
        self.tree.setLight(alnp)

        self.taskMgr.add(self.move_light, "move-light")

    def move_light(self, task):
        ft = globalClock.getFrameTime()

        self.light_model.setPos(cos(ft)*4, sin(ft)*4, 0)

        return task.cont


game = PointAndAmbientLight()
game.run()