from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from panda3d.core import OrthographicLens, TextureStage


configVars = """
win-size 1280 720
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)

key_map = {
    "left": False,
    "right": False
}


def update_key_map(control_name, control_state, entity, walking):
    key_map[control_name] = control_state
    if walking:
        entity.find('**/+SequenceNode').node().loop(True, 0, 9)
    else:
        entity.find('**/+SequenceNode').node().loop(True, 10, 19)

    if control_name == "left":
        entity.setTexScale(TextureStage.getDefault(), -1, 1)
    elif control_name == "right":
        entity.setTexScale(TextureStage.getDefault(), 1, 1)


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0.1, 0.1, 0.1, 1)

        self.jack = self.loader.loadModel("assets/Jack/Jack")
        self.jack.setScale(0.3)
        self.jack.reparentTo(self.render)

        self.jack.find('**/+SequenceNode').node().loop(True, 10, 19)
        # self.jack.find('**/+SequenceNode').node().loop(True, 0, 9)

        lens = OrthographicLens()
        lens.setFilmSize(1280, 720)
        lens.setNearFar(-50, 50)
        self.cam.node().setLens(lens)

        self.accept("arrow_left", update_key_map, ["left", True, self.jack, True])
        self.accept("arrow_left-up", update_key_map, ["left", False, self.jack, False])
        self.accept("arrow_right", update_key_map, ["right", True, self.jack, True])
        self.accept("arrow_right-up", update_key_map, ["right", False, self.jack, False])

        self.taskMgr.add(self.move_jack, "move-jack")

        self.x = 0
        self.speed = 200

    def move_jack(self, task):
        dt = globalClock.getDt()

        if key_map["left"]:
            self.x -= self.speed * dt
        if key_map["right"]:
            self.x += self.speed * dt

        self.jack.setPos(self.x, 0, 0)

        return task.cont




game = MyGame()
game.run()

