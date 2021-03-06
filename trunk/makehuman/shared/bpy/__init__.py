#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
**Project Name:**      MakeHuman

**Product Home Page:** http://www.makehuman.org/

**Code Home Page:**    http://code.google.com/p/makehuman/

**Authors:**           Thomas Larsson

**Copyright(c):**      MakeHuman Team 2001-2013

**Licensing:**         AGPL3 (see also http://www.makehuman.org/node/318)

**Coding Standards:**  See http://www.makehuman.org/node/165

Abstract
--------
Blender API mockup: bpy
This package is used by the FBX exporter. The actual exporter is located in the tools
directory and is a Blender plugin. By adding a few classes, the exporter can be tricked
to believe that it runs under Blender when it is actually invoked by MakeHuman.

"""

from . import types
from . import props
from . import utils
from . import path

#------------------------------------------------------------------
#   Context
#------------------------------------------------------------------

class Context:
    def __init__(self, scn):
        self.scene = scn
        self.object = None
        
#------------------------------------------------------------------
#   Data
#------------------------------------------------------------------
    
class Data:
    def __init__(self):
        self.objects = []
        self.meshes = []
        self.materials = []
        self.textures = []
        self.images = []
        self.armatures = []
        self.bones = []
        self.cameras = []
        self.lamps = []
        self.scenes = []
        self.actions = []

#------------------------------------------------------------------
#   Data
#------------------------------------------------------------------

def initialize():
    global context, data
    types.initialize()
    data = Data()
    scn = types.Scene()
    data.scenes.append(scn)
    context = Context(scn)
    
    
def addMesh(name, stuff, isStuff=True):
    global data
    me = types.Mesh(name)
    data.meshes.append(me)
    if isStuff:
        me.fromStuff(stuff)
    else:
        me.fromMesh(stuff)
    ob = types.Object(name, me, stuff)    
    data.objects.append(ob)
    context.scene.objects.append(ob)
    return ob
    

def addRig(name, boneInfo):
    global data
    amt = types.Armature(name, boneInfo)
    data.armatures.append(amt)
    rig = types.Object(name, amt)
    data.objects.append(rig)
    context.scene.objects.append(rig)
    return rig
    

initialize()
usingMakeHuman = True
