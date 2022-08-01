from pyglet.gl import *
from pyglet.window import key, mouse
import math


class Model:

    def get_tex(self,file):
        tex = pyglet.image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self, cubes):


        self.batch = pyglet.graphics.Batch()

        tex_coords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))

        for cube in cubes:
            coords, color = cube
            # import pdb
            # pdb.set_trace()
            for coord in coords:
                x,y,z = coord
                X,Y,Z = x+1,y+1,z+1

                parent_dir = './common/'
                top = self.get_tex(parent_dir + color + '.png')
                side = self.get_tex(parent_dir + color + '.png')
                bottom = self.get_tex(parent_dir + color + '.png')

                self.batch.add(4,GL_QUADS,side,('v3f',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),tex_coords)
                self.batch.add(4,GL_QUADS,side,('v3f',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),tex_coords)
                self.batch.add(4,GL_QUADS,bottom,('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),tex_coords)
                self.batch.add(4,GL_QUADS,top,('v3f',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),tex_coords)
                self.batch.add(4,GL_QUADS,side,('v3f',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),tex_coords)
                self.batch.add(4,GL_QUADS,side,('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),tex_coords)


    def draw(self):
        self.batch.draw()



class Player:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def mouse_motion(self,dx,dy):
        dx/=8; dy/=8; self.rot[0]+=dy; self.rot[1]-=dx
        if self.rot[0]>90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90

    def update(self,dt,keys):
        s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)
        if keys[key.UP]: self.pos[0]+=dx; self.pos[2]-=dz
        if keys[key.DOWN]: self.pos[0]-=dx; self.pos[2]+=dz
        if keys[key.LEFT]: self.pos[0]-=dz; self.pos[2]-=dx
        if keys[key.RIGHT]: self.pos[0]+=dz; self.pos[2]+=dx

        if keys[key.SPACE]: self.pos[1]+=s
        if keys[key.ENTER]: self.pos[1]-=s


class Window(pyglet.window.Window):

    def push(self,pos,rot): glPushMatrix(); glRotatef(-rot[0],1,0,0); glRotatef(-rot[1],0,1,0); glTranslatef(-pos[0],-pos[1],-pos[2],)
    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    def set2d(self): self.Projection(); gluOrtho2D(0,self.width,0,self.height); self.Model()
    def set3d(self): self.Projection(); gluPerspective(70,self.width/self.height,0.05,1000); self.Model()

    def setLock(self,state): self.lock = state; self.set_exclusive_mouse(state)
    lock = False; mouse_lock = property(lambda self:self.lock,setLock)

    def __init__(self,*args,**kwargs):
        cubes = kwargs.pop('cubes')
        super(Window, self).__init__(*args,**kwargs)
        self.set_minimum_size(300,200)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

        self.model = Model(cubes)
        self.player = Player((20.5,10.5,25.5),(-30,0))
        # self.player = Player((0.5,1.5,1.5),(-30,0))

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE: self.close()
        elif KEY == key.E: self.mouse_lock = not self.mouse_lock

    def update(self,dt):
        self.player.update(dt,self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(self.player.pos,self.player.rot)
        self.model.draw()
        glPopMatrix()


def draw_shape(cubes):

    window = Window(width=854,height=480,caption='Minecraft',resizable=True, cubes=cubes)
    glClearColor(0.5,0.7,1,1)
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_CULL_FACE)
    pyglet.app.run()

#add all cubes from all shapes with color to one big list
def draw_shapes(shapes):
    cubes = []
    for shape in shapes:
        coords, color = shape
        cubes.append((coords,color))
    draw_shape(cubes)


def draw_shapes_spread(shapes, spread_factor):
    cubes = []
    for multiplier, shape in enumerate(shapes):
        # import pdb
        # pdb.set_trace()
        coords, color = shape
        spread_coords = []
        for coord in coords:
            #add to axis
            spread_coord = (coord[0] + multiplier * spread_factor, coord[1], coord[2])
            spread_coords.append(spread_coord)
        cubes.append((spread_coords,color))
    draw_shape(cubes)

#add all cubes from all shapes with color to one big list
def animate_shapes_spread(shapes):
    for i in range(10):
        draw_shapes_spread(shapes, i * 0.5)

#add all cubes from all shapes with color to one big list
def draw_shapes_one_each(shapes):
    new_shapes = []
    shapes.sort(key=lambda a: sum(b[1] for b in a[0]))
    for shape in shapes:
        new_shapes.append(shape)
        draw_shapes(new_shapes)

