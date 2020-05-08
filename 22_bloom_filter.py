from panda3d.core import loadPrcFileData

configVars = """
win-size 1280 720
fullscreen 0
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)

from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight, AmbientLight, NodePath
from math import sin, cos
from direct.filter.CommonFilters import CommonFilters


class LightsAndShadows(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0, 1)
        self.cam.setPos(0, -12, 0)

        self.trees = NodePath("trees")

        self.tree1 = self.loader.loadModel('my-models/christmas_tree')
        self.tree1.setPos(0, 0, -2.5)
        self.tree1.reparentTo(self.trees)

        self.tree2 = self.loader.loadModel('my-models/christmas_tree')
        self.tree2.setPos(4, 5, -2.5)
        self.tree2.reparentTo(self.trees)

        self.tree3 = self.loader.loadModel('my-models/christmas_tree')
        self.tree3.setPos(-4, 7, -2.5)
        self.tree3.reparentTo(self.trees)

        self.trees.reparentTo(self.render)

        self.floor = self.loader.loadModel('my-models/floor')
        self.floor.setPos(0, 0, -2.5)
        self.floor.reparentTo(self.render)

        self.light_model = self.loader.loadModel('models/misc/sphere')
        self.light_model.setScale(0.2, 0.2, 0.2)
        # self.light_model.setPos(4, -4, 0)
        self.light_model.reparentTo(self.render)

        plight = PointLight("plight")
        plight.setShadowCaster(True, 1024, 1024)
        self.render.setShaderAuto()
        plnp = self.light_model.attachNewNode(plight)
        # plight.setAttenuation((1, 0, 0)) # constant, linear, and quadratic.
        self.trees.setLight(plnp)

        alight = AmbientLight("alight")
        alight.setColor((0.04, 0.04, 0.04, 1))
        alnp = self.render.attachNewNode(alight)
        self.trees.setLight(alnp)

        self.floor.setLight(plnp)
        self.floor.setLight(alnp)

        filters = CommonFilters(self.win, self.cam)
        filters.setBloom(size="large")

        self.taskMgr.add(self.move_light, "move-light")

    def move_light(self, task):
        ft = globalClock.getFrameTime()

        self.light_model.setPos(cos(ft)*4, sin(ft)*4, 0)

        return task.cont


game = LightsAndShadows()
game.run()