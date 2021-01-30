from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from direct.actor.Actor import Actor

configVars = """
win-size 1280 720
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0.1, 0.1, 0.1, 1)
        self.cam.setPos(0, -60, 0)

        self.arm = Actor("my-models/boneTest_textured2", {"anim1": "my-models/boneTest-ArmatureAction"})
        # self.arm.reparentTo(self.render)
        self.arm.loop("anim1")

        # arm1 = self.render.attachNewNode("arm1")
        # arm1.setPos(0, 0, 5)
        # self.arm.instanceTo(arm1)

        for i in range(5):
            arm = self.render.attachNewNode("Arm" + str(i + 1))
            arm.setPos(i * 5, 0, 0)
            self.arm.instanceTo(arm)

        self.arm2 = self.render.get_child(2)
        self.arm2.setPos(self.arm2.getPos().x, self.arm2.getPos().y, 10)

        # for index, c in enumerate(self.render.get_children()):
        #     print(index, c)

        self.taskMgr.add(self.rotate_arm2, "rotate-arm-2")
        self.angle = 0

    def rotate_arm2(self, task):
        self.arm2.setH(self.angle)
        self.angle += 1
        if self.angle > 359:
            self.angle = 0
        return task.cont


game = MyGame()
game.run()
