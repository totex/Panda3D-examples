from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from direct.directutil import Mopath
from direct.interval.MopathInterval import *
from direct.filter.CommonFilters import CommonFilters

configVars = """
win-size 1280 720
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0, 1)
        self.cam.setPos(0, -80, 0)

        self.sphere = self.loader.loadModel('models/misc/sphere')
        self.sphere.setScale(0.5)
        self.sphere.reparentTo(self.render)

        my_curve = Mopath.Mopath()
        my_curve.loadFile("my-models/curvey")

        my_interval = MopathInterval(my_curve, self.sphere, name="my-path", duration=8)
        # my_interval.start()
        my_interval.loop()

        filters = CommonFilters(self.win, self.cam)
        filters.setBloom(size="medium")

        print(my_curve.xyzNurbsCurve.getNumKnots())
        print(my_curve.xyzNurbsCurve.getOrder())
        print(my_curve.xyzNurbsCurve.getNumCvs())
        print(my_curve.xyzNurbsCurve.getKnots())



game = MyGame()
game.run()
