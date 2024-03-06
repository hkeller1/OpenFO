import FreeCAD,FreeCADGui,Part
import json
import Mesh
import os
import Rotate_Class
import Translate_Class
import PySide.QtCore as QtCore

class PositionTaskPanel:
   def __init__(self):
       # this will create a Qt widget from our ui file
       self.form = FreeCADGui.PySideUic.loadUi(r"C:\Users\hanam\AppData\Roaming\FreeCAD\Mod\Hana_workbenchFO\TaskPosition.ui")
       self.form.setObjectName("PositionTaskPanel")
       self.form.setWindowTitle("Position")
       
       FreeCADGui.ActiveDocument.ActiveView.fitAll()
       
       QtCore.QObject.connect(self.form.translateButton, QtCore.SIGNAL("clicked()"), self.move)
       QtCore.QObject.connect(self.form.rotateButton, QtCore.SIGNAL("clicked()"), self.rotate)
       QtCore.QObject.connect(self.form.leftButton, QtCore.SIGNAL("clicked()"), self.left)
       QtCore.QObject.connect(self.form.topButton, QtCore.SIGNAL("clicked()"), self.top)
       QtCore.QObject.connect(self.form.frontButton, QtCore.SIGNAL("clicked()"), self.front)
        
   def accept(self):
       print("Move on to Landmark")
       FreeCADGui.Control.closeDialog()
   
   def top(self):
       self.orientation = 1
       FreeCADGui.ActiveDocument.ActiveView.viewTop()
   def left(self):
       self.orientation = 2
       FreeCADGui.ActiveDocument.ActiveView.viewLeft()
   def front(self):
       self.orientation = 3
       FreeCADGui.ActiveDocument.ActiveView.viewFront()
   
   def read_orientation (self):
       if self.orientation == 1:
           FreeCADGui.ActiveDocument.ActiveView.viewLeft()
           print("1")
       elif self.orientation == 2:
           FreeCADGui.ActiveDocument.ActiveView.viewTop()
           print("2")
       elif self.orientation == 3:
           FreeCADGui.ActiveDocument.ActiveView.viewFront()
           print("3")

   def move(self):
       """Assign the selected file."""
       #read_orientation()
       mover = Translate_Class.FOTranslate()
       mover.Activated()
        
   def rotate(self):
       #self.read_orientation()
       rotater = Rotate_Class.FORotate()
       rotater.Activated()



#panel = ImportTaskPanel()
#FreeCADGui.Control.showDialog(panel)