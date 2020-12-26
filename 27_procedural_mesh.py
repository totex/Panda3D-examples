from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, OrthographicLens
from panda3d.core import GeomVertexFormat, GeomVertexData, TransparencyAttrib
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter, GeomNode

configVars = """
win-size 1280 720
show-frame-rate-meter 1
"""

loadPrcFileData("", configVars)


def create_colored_rect(x, z, width, height, colors=None):
    _format = GeomVertexFormat.getV3c4()
    vdata = GeomVertexData('square', _format, Geom.UHDynamic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    color = GeomVertexWriter(vdata, 'color')

    vertex.addData3(x, 0, z)
    vertex.addData3(x + width, 0, z)
    vertex.addData3(x + width, 0, z + height)
    vertex.addData3(x, 0, z + height)

    if colors:
        if len(colors) < 4:
            colors = (1.0, 1.0, 1.0, 1.0)
        color.addData4f(colors)
        color.addData4f(colors)
        color.addData4f(colors)
        color.addData4f(colors)
    else:
        color.addData4f(1.0, 0.0, 0.0, 1.0)
        color.addData4f(0.0, 1.0, 0.0, 1.0)
        color.addData4f(0.0, 0.0, 1.0, 1.0)
        color.addData4f(1.0, 1.0, 1.0, 1.0)

    tris = GeomTriangles(Geom.UHDynamic)
    tris.addVertices(0, 1, 2)
    tris.addVertices(2, 3, 0)

    square = Geom(vdata)
    square.addPrimitive(tris)
    return square


def create_textured_rect(x, z, width, height):
    _format = GeomVertexFormat.getV3t2()
    vdata = GeomVertexData('square', _format, Geom.UHDynamic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    texcoord = GeomVertexWriter(vdata, 'texcoord')

    vertex.addData3(x, 0, z)
    vertex.addData3(x + width, 0, z)
    vertex.addData3(x + width, 0, z + height)
    vertex.addData3(x, 0, z + height)

    texcoord.addData2f(0.0, 0.0)
    texcoord.addData2f(1.0, 0.0)
    texcoord.addData2f(1.0, 1.0)
    texcoord.addData2f(0.0, 1.0)

    tris = GeomTriangles(Geom.UHDynamic)
    tris.addVertices(0, 1, 2)
    tris.addVertices(2, 3, 0)

    square = Geom(vdata)
    square.addPrimitive(tris)
    return square


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0.1, 0.1, 0.1, 1)

        square1 = create_colored_rect(0, 0, 200, 200)
        square2 = create_colored_rect(350, 100, 200, 200, (0, 0, 1, 1))
        square3 = create_colored_rect(-640, -360, 200, 200, (0, 1, 0, 1))

        gnode = GeomNode('square')
        gnode.addGeom(square1)
        gnode.addGeom(square2)
        gnode.addGeom(square3)

        self.render.attachNewNode(gnode)

        gnode2 = GeomNode('square2')
        textured_rect = create_textured_rect(-320, 0, 200, 280)
        gnode2.addGeom(textured_rect)

        texture = self.loader.loadTexture("assets/images/PlayerShip.png")
        ship = self.render.attachNewNode(gnode2)
        ship.setTransparency(TransparencyAttrib.MAlpha)
        ship.setTexture(texture)

        lens = OrthographicLens()
        lens.setFilmSize(1280, 720)
        lens.setNearFar(-50, 50)
        self.cam.setPos(0, 0, 0)
        self.cam.node().setLens(lens)


game = MyGame()
game.run()
