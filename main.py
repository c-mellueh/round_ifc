from PySide6 import QtWidgets,QtCore
import ifcopenshell
import os
class Ui_MainWindow(object):

   def setupUi(self, MainWindow):
      MainWindow.setObjectName("MainWindow")
      MainWindow.resize(599, 257)
      self.centralwidget = QtWidgets.QWidget(MainWindow)
      self.centralwidget.setObjectName("centralwidget")
      self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
      self.gridLayout.setObjectName("gridLayout")
      self.formLayout = QtWidgets.QFormLayout()
      self.formLayout.setObjectName("formLayout")
      self.button_file = QtWidgets.QPushButton(self.centralwidget)
      self.button_file.setObjectName("button_file")
      self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.button_file)
      self.button_save = QtWidgets.QPushButton(self.centralwidget)
      self.button_save.setObjectName("button_save")
      self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.button_save)
      self.file_path = QtWidgets.QLineEdit(self.centralwidget)
      self.file_path.setObjectName("file_path")
      self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.file_path)
      self.save_path = QtWidgets.QLineEdit(self.centralwidget)
      self.save_path.setObjectName("save_path")
      self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.save_path)
      self.label = QtWidgets.QLabel(self.centralwidget)
      self.label.setObjectName("label")
      self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
      self.decimal_place = QtWidgets.QSpinBox(self.centralwidget)
      self.decimal_place.setProperty("value", 3)
      self.decimal_place.setObjectName("decimal_place")
      self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.decimal_place)
      self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
      self.progress_bar.setProperty("value", 0)
      self.progress_bar.setObjectName("progress_bar")
      self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.progress_bar)
      self.button_start = QtWidgets.QPushButton(self.centralwidget)
      self.button_start.setObjectName("button_start")
      self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.button_start)
      self.status = QtWidgets.QLabel(self.centralwidget)
      self.status.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
      self.status.setIndent(27)
      self.status.setObjectName("status")
      self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.status)
      self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
      self.groupBox.setObjectName("groupBox")
      self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
      self.gridLayout_2.setObjectName("gridLayout_2")
      self.cartesian_point = QtWidgets.QCheckBox(self.groupBox)
      self.cartesian_point.setChecked(True)
      self.cartesian_point.setObjectName("cartesian_point")
      self.gridLayout_2.addWidget(self.cartesian_point, 0, 0, 1, 1)
      self.cartesian_point_list = QtWidgets.QCheckBox(self.groupBox)
      self.cartesian_point_list.setChecked(True)
      self.cartesian_point_list.setObjectName("cartesian_point_list")
      self.gridLayout_2.addWidget(self.cartesian_point_list, 0, 1, 1, 1)
      self.rectangle_profile_def = QtWidgets.QCheckBox(self.groupBox)
      self.rectangle_profile_def.setChecked(True)
      self.rectangle_profile_def.setObjectName("rectangle_profile_def")
      self.gridLayout_2.addWidget(self.rectangle_profile_def, 0, 2, 1, 1)
      self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
      self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
      MainWindow.setCentralWidget(self.centralwidget)
      self.statusbar = QtWidgets.QStatusBar(MainWindow)
      self.statusbar.setObjectName("statusbar")
      MainWindow.setStatusBar(self.statusbar)

      self.retranslateUi(MainWindow)
      QtCore.QMetaObject.connectSlotsByName(MainWindow)

   def retranslateUi(self, MainWindow):
      _translate = QtCore.QCoreApplication.translate
      MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
      self.button_file.setText(_translate("MainWindow", "File"))
      self.button_save.setText(_translate("MainWindow", "Save As"))
      self.label.setText(_translate("MainWindow", "Decimal place"))
      self.button_start.setText(_translate("MainWindow", "Start"))
      self.status.setText(_translate("MainWindow", "Idle"))
      self.groupBox.setTitle(_translate("MainWindow", "Modifiable entities"))
      self.cartesian_point.setText(_translate("MainWindow", "IfcCartesianPoint"))
      self.cartesian_point_list.setText(_translate("MainWindow", "IfcCartesianPointList3D"))
      self.rectangle_profile_def.setText(_translate("MainWindow", "IfcRectangleProfileDef"))
      self.click_events()

   def click_events(self):
      self.worker = Worker(ui)
      self.button_file.clicked.connect(self.get_file_name)
      self.button_save.clicked.connect(self.set_save_name)
      self.worker.updateProgress.connect(self.set_progress_bar)
      self.button_start.clicked.connect(self.worker.start)


   def set_progress_bar(self,progress):
      self.progress_bar.setValue(progress)

   def get_file_name(self):
      file_path = \
      QtWidgets.QFileDialog.getOpenFileName(caption="IFC Datei", filter="IFC Datei (*.ifc)",
                                                        selectedFilter="IFC Datei (*.ifc)")[0]
      file_name, extensinsion = os.path.splitext(file_path)
      if file_name != "":
         self.file_path.setText(file_path)
         if self.save_path.text() == "":
            self.save_path.setText(file_name + "_rounded.ifc")

   def set_save_name(self):

      file_path = QtWidgets.QFileDialog.getSaveFileName(caption="IFC Datei", filter="IFC Datei (*.ifc)",
                                                        selectedFilter="IFC Datei (*.ifc)")[0]
      if not file_path.endswith("_rounded.ifc") and file_path != "":
         file_path += "_rounded.ifc"
      self.save_path.setText(file_path)


class Input():

   def __init__(self,ui:Ui_MainWindow):
      self.file_path = ui.file_path.text()
      self.save_path = ui.save_path.text()
      self.decimals = ui.decimal_place.value()
      self.cartesian_point = ui.cartesian_point.isChecked()
      self.cartesian_point_list = ui.cartesian_point_list.isChecked()
      self.rectangle_profile = ui.rectangle_profile_def.isChecked()

class TestInput():

   def __init__(self):
      self.file_path = "/home/christoph/PycharmProjects/CityGML2IFC/Result_with_transform.ifc"
      self.save_path = "/home/christoph/PycharmProjects/CityGML2IFC/Result_with_transform_rounded.ifc"
      self.decimals = 3
      self.cartesian_point = True
      self.cartesian_point_list = True
      self.rectangle_profile = True

class Worker(QtCore.QThread):
   updateProgress = QtCore.Signal(int)

   def __init__(self, ui: Ui_MainWindow):
      QtCore.QThread.__init__(self)
      self.ui = ui

   def run(self):
      input_informations = Input(self.ui)



      self.ui.status.setText("Status: Processing")

      generator = round_elements(input_informations)

      for items, total in generator:
         self.updateProgress.emit(int(items / total * 100))

      self.updateProgress.emit(100)

      self.ui.status.setText("Status: Done!")

def round_elements(informations:TestInput):

   file = informations.file_path
   print("File {}".format(file))
   print("Save {}".format(informations.save_path))
   ifc = ifcopenshell.open(file)

   decimals = informations.decimals

   modifiable_objects = []


   if informations.cartesian_point:
      cart_points = []

      try:
         cart_points = ifc.by_type("IFCCARTESIANPOINT", include_subtypes=True)
      except:
         print("no CartesianPoints")
      modifiable_objects += cart_points

   if informations.cartesian_point_list:
      point_lists = []

      try:
         point_list = ifc.by_type("IFCCARTESIANPOINTLIST3D", include_subtypes=True)
      except:
         print("no IFCCARTESIANPOINTLIST3D")
      modifiable_objects += point_lists

   if informations.rectangle_profile:
      rec_profiles = []

      try:
         rec_profile = ifc.by_type("IFCRECTANGLEPROFILEDEF", include_subtypes=True)
      except:
         print("no IFCRECTANGLEPROFILEDEF")
      modifiable_objects += rec_profiles


   for i,el in enumerate(modifiable_objects):
      yield(i,len(modifiable_objects))
      if el.is_a('IFCCARTESIANPOINT'):
         coordinate_tuple = el.Coordinates
         coordinate_list = []
         for value in coordinate_tuple:
            coordinate_list.append(float(round(value, decimals)))
         el.Coordinates = tuple(coordinate_list)

      if el.is_a("IFCCARTESIANPOINTLIST3D"):
         coordinate_list_tuple = list(el.CoordList)
         coordinate_list_list = []
         for coordinate_tuple in coordinate_list_tuple:
            coordinate_list = []
            for value in coordinate_tuple:
               value = float(round(value,decimals))
               coordinate_list.append(value)
            coordinate_list_list.append(coordinate_list)
         el.CoordList = tuple(coordinate_list_list)

      if el.is_a("IFCRECTANGLEPROFILEDEF"):
         el.XDim = float(round(el.XDim, decimals))
         el.YDim = float(round(el.YDim,decimals))

   print("HIER")
   path = informations.save_path
   print(path)
   ifc.write(path)
   print("written")

if __name__ == "__main__":
   import sys

   application = QtWidgets.QApplication(sys.argv)
   window = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(window)
   window.show()
   sys.exit(application.exec())