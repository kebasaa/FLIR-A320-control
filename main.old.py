#-------------------------------------------------------------------------------
# Name:        FLIR A320 control software
# Purpose:	   This software controls the FLIR A320
#
# Author:      Jonathan D. Müller
#
# Created:     03/09/2017
# Copyright:   (c) Jonathan D. Müller 2017
# Licence:     GPL
#-------------------------------------------------------------------------------

# System stuff
import datetime, ctypes
from time import strftime # For logging
from time import sleep
import json # used to parse config.json
from os.path import expanduser # for user directory
import os.path
import os

# Import Qt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Import the user interface
from Interface import *
import functions.flir
flir = functions.flir.FLIR

# Logging
import logging
import sys
log = logging.getLogger('root')
log.setLevel(logging.DEBUG)
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(levelname)8s %(module)15s: %(message)s')
stream.setFormatter(formatter)
log.addHandler(stream)

class Main(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        log.info("Starting FLIR program")
        self.cam = None
        self.currentImg = None
        self.logFolder = ''
		
        # initialise the data list: 1x Date, 2x Arduino, 4x 6262
        #self.data = [float('nan')]*7
        # These threads run in the background
        self.initUI()
        
        self.flir_running = False
        self.logging_running = False
		
        # set up timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timed_tasks)
		
        # Automatically start logging
        self.logging_autostart()

    def initUI(self):
        # Get all settings
        # First read them
        self.get_config()
        self.logFolder = self.config["log_folder"]
        # Then put settings in the UI
        self.ui.logfolder.setText(self.logFolder)
        self.ui.IntervalTime.setText(str(self.config["log_interval"]))
        self.ui.flirIP.setText(self.config["flir_IP"])
		
        # Check for COM ports and add them
        #
        self.ui.connect.clicked.connect(self.connectFLIR) # & flirIP
        self.ui.autofocusFull.clicked.connect(self.autofocusFull)
        self.ui.autofocusQuick.clicked.connect(self.autofocusQuick)
        self.ui.shootNow.clicked.connect(self.shootNow)
        self.ui.setAtmT.clicked.connect(self.setAtmT) #atmT
        self.ui.setAmbT.clicked.connect(self.setAmbT) #ambT
        self.ui.setDist.clicked.connect(self.setDist) #dist
        self.ui.setRH.clicked.connect(self.setRH)     #rh
        self.ui.setEmissivity.clicked.connect(self.setEmissivity) #emissivity
        self.ui.IntervalSet.clicked.connect(self.setInterval) #IntervalTime
        self.ui.chooseFolderButton.clicked.connect(self.folderChooser)
        self.ui.LogStart.clicked.connect(self.logStart)
        # put in some new default
        #self.ui.IntervalTime.setText("240")

    def timed_tasks(self):
        self.connectFLIRquick()
        try:
            self.shootNow()
        except:
            pass
        else:
            self.connectFLIRquick()
		
    def get_config(self):
        with open('settings.json') as config_file:
            self.config = json.load(config_file)
			
    def set_config(self):
        self.config["flir_IP"] = self.ui.flirIP.text()
        self.config["log_interval"] = int(self.ui.IntervalTime.text())
        self.config["log_folder"] = self.logFolder
        with open('settings.json', 'w') as cfile:
            cfile.write(json.dumps(self.config))
		
    def logging_autostart(self):
        self.connectFLIR()
        self.logStart()
		
    def connectFLIR(self):
        if(self.flir_running == True):
            log.info("Disconnecting & rebooting FLIR")
            try:
                self.cam.reboot()
                self.cam.close()
                del self.cam
                self.ui.connect.setText("Connect")
                log.info("Camera rebooting")
                #sleep(15)
            except:
                pass
            self.flir_running = False
        else:
            log.info("Connecting FLIR " + self.ui.flirIP.text())
            self.cam = flir(self.ui.flirIP.text())
            try:
                self.cam.connect()
            except:
                pass
            else:
                log.info("Setting camera date & time")
                self.cam.setDateTime()
                self.ui.connect.setText("Disconnect")
                self.flir_running = True
                log.info("Camera ready")
				
    def rebootFLIR(self):
        if(self.flir_running == True):
            log.info("Disconnecting & rebooting FLIR")
            try:
                self.cam.reboot()
                self.cam.close()
                del self.cam
                self.ui.connect.setText("Connect")
                log.info("Rebooting")
                #sleep(45)
            except:
                pass
            self.flir_running = False
        else:
            log.info("Camera not running")
            try:
                self.cam.close()
                del self.cam
                self.ui.connect.setText("Connect")
            except:
                pass
				
    def connectFLIRquick(self):
        if(self.flir_running == True):
            log.info("Disconnecting FLIR")
            try:
                self.cam.reboot() ########################################## Don't reboot every time?
                self.cam.close()
                del self.cam
                self.ui.connect.setText("Connect")
            except:
                pass
            self.flir_running = False
        else:
            log.info("Connecting FLIR " + self.ui.flirIP.text())
            self.cam = flir(self.ui.flirIP.text())
            try:
                self.cam.connect()
            except:
                pass
            else:
                self.ui.connect.setText("Disconnect")
                self.flir_running = True

    def autofocusFull(self):
        log.info("Full autofocus")
        try:
            self.cam.slowFocus()
        except:
            QMessageBox.warning(None,"Connect","Please connect the camera.")

    def autofocusQuick(self):
        log.info("Quick autofocus")
        try:
            self.cam.quickFocus()
        except:
            QMessageBox.warning(None,"Connect","Please connect the camera.")

    def shootNow(self):
        log.info("shoot to " + self.logFolder)
        folder = ''
        if(self.logFolder == ''):
            folder = self.logFolder
        else:
            folder = self.logFolder + "/"
        #self.currentImg = self.cam.shootJPG(folder)

        while(True):
            # Check if the camera is already running. If not, boot it up & connect
            if(self.flir_running == True):
                log.info("Camera is connected") #pass
            else:
                log.info("Connecting to camera now or rebooting it")
                self.connectFLIR()
                if(self.flir_running == False):
                    sleep(30)
                    log.info("Failed to reboot, next while loop")
                    continue # Failed to reboot, next while loop
            # Now, after connecting, I can try to shoot the image
            try:
                log.info("Attempting to shoot image")
                self.currentImg = self.cam.shootJPG(folder)
            except:
                #QMessageBox.warning(None,"Connect","Please connect the camera.")
                log.info("Failed to shoot image: Send reboot instructions")
                self.rebootFLIR()
                #log.info("Reboot done, waiting 45s")
                #sleep(45)
                #continue # next loop to try to connect & shoot
                break
            else:
                # Shooting the image succeeded.
                #statinfo = os.stat(self.currentImg)
                #filesize = statinfo.st_size
                filesize = os.path.getsize(self.currentImg)
                log.info("Created file " + self.currentImg + " with size " + str(filesize/1000) + "kB")
                if(filesize < 10 or self.currentImg == ""): # The file is smaller than 10 bytes (my random cutoff value), meaning it is probably invalid, then the camera needs to reboot
                    log.info("Empty/Missing file: Rebooting camera")
                    self.rebootFLIR()
                    sleep(30)
                    break # Don't shoot an image if it rebooting #NEW
                else: # This is in case the image was ok
                    log.debug("File size: " + str(filesize/1000) + "kB")
                    break # Break the while loop
        # Now show the resulting image in the GUI
        image = QtGui.QImage(self.currentImg)
        image = image.scaled(640,480, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
        self.ui.currentImg.setPixmap(QtGui.QPixmap.fromImage(image))
		
    def setAtmT(self):
        log.info("set atmospheric T " + self.ui.atmT.text())
        try:
            self.cam.setAtmT(float(self.ui.atmT.text()))
        except:
            QMessageBox.warning(None,"Connect","Please connect the camera.")

    def setAmbT(self):
        log.info("set ambient T " + self.ui.ambT.text())
        try:
            self.cam.setAmbT(float(self.ui.ambT.text()))
        except:
            QMessageBox.warning(None,"Connect","Please connect the camera.")

    def setDist(self):
        log.info("set distance " + self.ui.dist.text())
        try:
            self.cam.setDist(float(self.ui.dist.text()))
        except:
            QMessageBox.warning(None,"Connect","Please connect the camera.")

    def setRH(self):
        log.info("set relative humidity " + self.ui.rh.text())
        self.cam.setRH(float(self.ui.rh.text())/100)
        try:
            self.cam.setRH(float(self.ui.rh.text())/100)
        except:
            QMessageBox.warning(None,"Connect","Please connect the camera.")

    def setEmissivity(self):
        log.info("set emissivity " + self.ui.emissivity.text())
        try:
            self.cam.setEmiss(float(self.ui.emissivity.text()))
        except:
            QMessageBox.warning(None,"Connect","Please connect the camera.")
		
    def setInterval(self):
        log.info("set interval " + self.ui.IntervalTime.text())
        try:
            pass
        except:
            QMessageBox.warning(None,"Connect","Please connect the camera.")
		
    def folderChooser(self):
        fname = QFileDialog.getExistingDirectory(self, "Select Directory",
                            expanduser("~\Documents"))
        if(fname == ""):
            log.debug("No folder selected")
            QMessageBox.warning(None,"No folder selected","Please select a log folder.")
        else:
            log.info("Log data to: " + fname)
            self.logFolder = fname
            self.ui.logfolder.setText(fname)

    def logStart(self):
        if(self.logging_running == True):
            log.info("Stop logging")
            self.ui.LogStart.setText("Start logging")
            self.timer.stop()
            self.logging_running = False
        else:
            # Check if devices are connected
            if(self.flir_running == True):
                # Run every X seconds
                #self.autofocusFull() # first focus
                self.ui.LogStart.setText("Stop logging")
                self.timer.start(int(self.ui.IntervalTime.text())*60*1000) #convert ms into min
                self.logging_running = True
                self.connectFLIR()
            else:
                QMessageBox.warning(None,"Connect","Please connect the camera.")
			
    def closeEvent(self, event): # This is when the window is clicked to close
        log.info("Shutting down application")
        self.set_config()
        try:
            self.cam.close()
        except:
            pass
        log.info("Shutdown completed")
        log.info('------------------')
        event.accept()
			
		
# Show the image
if __name__ == "__main__":
    # This tells Windows to use my icon
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	
    app = QApplication(sys.argv)
    myapp = Main()
    myapp.show()
	
    sys.exit(app.exec_())