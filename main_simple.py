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
import datetime
from time import strftime # For logging
from os.path import expanduser # for user directory
import os.path

# Import functions
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

class Main():
    def __init__(self, parent=None):
        log.info("Starting FLIR A320 control program")
		# Initialise
        self.cam = flir('192.168.1.10')
        log.info("Connecting")
        self.cam.connect()
        log.info("Setting date & time")
        self.cam.setDateTime()

    def run(self):
        log.info("Focussing")
        self.cam.slowFocus()
        log.info("Shooting")
        self.cam.shootJPG('')
        self.cam.shootFFF('')
        log.info("Finished")
        self.cam.close()

 
		
# Show the image
if __name__ == "__main__":
    # This tells Windows to use my icon
    #myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    #ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	
    #app = QApplication(sys.argv)
    myapp = Main()
    myapp.run()
    #myapp.show()
	
    #sys.exit(app.exec_())