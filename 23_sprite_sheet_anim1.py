from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from panda3d.core import TextureStage, SamplerState, TransparencyAttrib

configVars = """
win-size 1280 720
show-frame-rate-meter 1
textures-power-2 0
"""

loadPrcFileData("", configVars)


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0.1, 0.1, 0.1, 1)
        self.cam.setPos(0, -5, 0)

        self.plane = self.loader.loadModel("assets/eggs/plane2x2")
        self.tex = self.loader.loadTexture("assets/images/zombie.png")
        self.plane.setTexture(self.tex)
        self.tex.setMagfilter(SamplerState.FT_nearest)
        self.plane.setTransparency(TransparencyAttrib.MAlpha)
        self.plane.reparentTo(self.render)

        self.tx = 0.0
        self.tx_offset = 1 / 6
        self.texture_update = 0

        self.taskMgr.add(self.update_texture, "Update texture")

    def update_texture(self, task):
        self.plane.setTexOffset(TextureStage.getDefault(), self.tx, 0)

        self.texture_update += 1
        if self.texture_update > 6:
            self.tx += self.tx_offset
            self.texture_update = 0

        return task.cont


game = MyGame()
game.run()
