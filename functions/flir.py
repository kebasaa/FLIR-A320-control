# With help from https://stackoverflow.com/questions/20484984/telnet-read-until-function-doesnt-work

import telnetlib , socket, ftplib, time, datetime

import logging
log = logging.getLogger('root')

class FLIR(object):
    def __init__(self, host):
        self.tn = None
        self.host = host # should be 192.168.1.10
        self.port = 23
        self.timeout = 2

    def connect(self):
        try :
            self.tn = telnetlib.Telnet(self.host,self.port,self.timeout)
        except socket.timeout :
            log.info("FLIR.connect() socket.timeout")
            return(False)
        # when connecting, just read until you reach the prompt
        #try:
            #self.tn.read_until(b'msc]',1)
            #self.tn.read_all()
        #except:
            #self.debug("TN connection error")
        #else:
            #self.nuc()
            #x = true
            #log.debug(x)
        #while(True):
        #    #log.debug("test2")
        #    try:
        #        self.tn.read_until(b'msc]',1)
        #        ##self.tn.read_all()
        #    except:
        #        self.debug("TN connection error")
        #    else:
        #        self.nuc()
        #        break
        else:
            while(True):
                try:
                    self.tn.read_until(b'msc]',1)
                    ##self.tn.read_all()
                except:
                    self.debug("TN connection error")
                else:
                    self.nuc()
                    break
        return(True)
		
    def disconnect(self):
        #try :
        #    self.tn = telnetlib.Telnet(self.host,self.port,self.timeout)
        #except socket.timeout :
        #    log.info("FLIR.connect() socket.timeout")
        # when connecting, just read until you reach the prompt
        #self.tn.read_until(b'msc]',1)
        self.tn.get_socket().shutdown(socket.SOCK_WR)
        self.tn.read_all()
        self.tn.close()
		
    # Set camera date and time to the computer time
    def setDateTime(self):
        # Set the date
        self.tn.write(b'date\n')
        self.tn.read_until(b'Enter new date (mm/dd/yyyy): ',1).decode('ascii')
        datenow = str(datetime.datetime.now().strftime('%m/%d/%Y')).encode('ascii') # store date string
        self.tn.write(datenow + b'\n')
        self.tn.read_until(b'>',1).decode('ascii')
        # Set the time
        self.tn.write(b'time\n')
        self.tn.read_until(b'Enter new time: ',1).decode('ascii')
        timenow = str(datetime.datetime.now().strftime('%H:%M:%S')).encode('ascii') # store time string
        self.tn.write(timenow + b'\n')
        self.tn.read_until(b'>',1).decode('ascii')
        # Check date and time
        #self.tn.write(b'date /T\n')
        #self.tn.write(b'time /T\n')
		
    # Set file format to file containing temperature data
    def setFormat(self):
        self.tn.write(b'rset .image.services.store.format \"JPEG+PNG\"\n')
        self.tn.read_until(b'>',1).decode('ascii')
		
    # Set relative humidity [0.0-1-0]
    def setRH(self, rh): # standard should be rh= 0.5
        self.tn.write(b'rset .image.sysimg.basicImgData.objectParams.relHum ' + str(rh).encode('ascii') + b'\n')
        self.tn.read_until(b'>',1).decode('ascii')
		
    # Set object distance [m]
    def setDist(self, distance):
        self.tn.write(b'rset .image.sysimg.basicImgData.objectParams.objectDistance ' + str(distance).encode('ascii') + b'\n')
        self.tn.read_until(b'>',1).decode('ascii')
		
    # Set ambient T [°C]
    def setAmbT(self, T):
        self.tn.write(b'rset .image.sysimg.basicImgData.objectParams.ambTemp ' + str(T + 273.15).encode('ascii') + b'\n')
        self.tn.read_until(b'>',1).decode('ascii')
		
    # Set atm T [°C]
    def setAtmT(self, T):
        self.tn.write(b'rset .image.sysimg.basicImgData.objectParams.atmTemp ' + str(T + 273.15).encode('ascii') + b'\n')
        self.tn.read_until(b'>',1).decode('ascii')
		
    # Set object emissivity (0.001-1.0)
    # Set atm T [°C]
    def setEmiss(self, E):
        self.tn.write(b'rset .image.sysimg.basicImgData.objectParams.emissivity ' + str(E).encode('ascii') + b'\n')
        self.tn.read_until(b'>',1).decode('ascii')
		
    # Set colour palette
    # pal can be: bw, iron, rainbow. I like iron the most
    def setPal(self, pal):
        self.tn.write(b'rset .image.sysimg.palette.readFile ' + pal.encode('ascii') + b'\n')
        self.tn.read_until(b'>',1).decode('ascii')
		
	# reboot command
    def reboot(self):
        self.tn.write(b'Restart\n')
        self.tn.read_until(b'>',1).decode('ascii')
        #self.disconnect()
        #self.tn.close()
		
	# NUC calibration
    def nuc(self):
        #self.tn.write(b'nuc\n') # perform NUC now
        self.tn.write(b'rset .tcomp.services.autoNuc.active true\n') # Set to automatically perform NUC
        #self.tn.write(b'rset .image.services.nuc.commit true\n')     # perform NUC now
        #time.sleep(10)
        self.tn.read_until(b'>',1).decode('ascii')
		
    def factoryReset(self):
        #self.tn.write(b'rset .system.restart true\n')
        self.tn.write(b'rset .power.actions.factorydefault true\n')
        self.tn.read_until(b'>',1).decode('ascii')
		
    # Quick Autofocus
    def quickFocus(self):
        self.tn.write(b'rset .system.focus.autofast true\n')
        time.sleep(2)
        self.tn.read_until(b'>',1).decode('ascii')

    # Slow but full autofocus
    def slowFocus(self):
        self.tn.write(b'rset .system.focus.autofull true\n')
        time.sleep(5)
        self.tn.read_until(b'>',1).decode('ascii')

    # Enable/disable overlay
    def overlay(self,enable):
        if(enable):
            print('enable')
            # Enable the legend
            self.tn.write(b'rset .image.services.store.overlay true\n')
            self.tn.read_until(b'>',1).decode('ascii')
        else:
            print('disable')
            # Disable the legend
            self.tn.write(b'rset .image.services.store.overlay false\n')
            self.tn.read_until(b'>',1).decode('ascii')
			
    # Enable/disable legend
    def legend(self,enable):
        if(enable):
            print('enable')
            # Enable the legend
            self.tn.write(b'rset .gui.system.hideGraphics false\n')
            self.tn.read_until(b'>',1).decode('ascii')
        else:
            print('disable')
            # Disable the legend
            self.tn.write(b'rset .gui.system.hideGraphics true\n')
            self.tn.read_until(b'>',1).decode('ascii')
		
    # Shoot image and transfer
    def shootJPG(self,path):
        #self.nuc()
        # shoot the image and store it temporarily on the camera
        self.tn.write(b'store -j temp.jpg\n')
        time.sleep(2)
        # Set the filename for storage on the computer, with date/time info
        filename = path + 'file-' + str(datetime.datetime.now().strftime('%Y%m%d-%H%M%S')) + '.jpg'
        # disconnect from telnet so as not to interfere with FTP
        self.tn.close()
        #self.disconnect()
        # Transmit file from the camera through FTP
        for i in range(0,10):
            try:
                ftp = ftplib.FTP(self.host, timeout=5)
                ftp.set_pasv(True)
                #ftp.set_pasv(False)
                ftp.login()
                ftp.cwd('/')
                ftp.retrbinary('RETR ' + 'temp.jpg', open(filename,'wb').write)
                ftp.quit()
                break
            except:
                log.info("FLIR.connect() FTP socket.timeout")
        # reconnect to telnet
        self.connect()
        # After successful transmission of the file, delete it on the camera
        self.tn.write(b'del temp.jpg\n')
        self.tn.read_until(b'>',1).decode('ascii')
        #self.nuc()
        return filename
		
    def shootFFF(self,path): #TODO: OPTION TO SET PATH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # TODO infor: https://developer.flir.com/forums/topic/metadata-format/
        # shoot the image and store it temporarily on the camera
        self.tn.write(b'store temp.fff\n')
        time.sleep(2)
        # Set the filename for storage on the computer, with date/time info
        filename = path + 'file-' + str(datetime.datetime.now().strftime('%Y%m%d-%H%M%S')) + '.fff'
        # Transmit file from the camera through FTP
        ftp = ftplib.FTP(self.host)
        ftp.set_pasv(False)
        ftp.login()
        ftp.cwd('/')
        ftp.retrbinary('RETR ' + 'temp.fff', open(filename,'wb').write)
        ftp.quit()
        # After successful transmission of the file, delete it on the camera
        self.tn.write(b'del temp.fff\n')
        self.tn.read_until(b'>',1).decode('ascii')
        return filename

    # Generic functions that allow more fine-grained, individual control of the camera
    def write(self,msg):
        self.tn.write(msg.encode('ascii') + b"\n")
        return True

    def read_until(self,value):
        return self.tn.read_until(value)


    def read_all(self):
        try :
            return self.tn.read_all().decode('ascii')
        except socket.timeout :
            print("read_all socket.timeout")
            return False

    def close(self):
        try:
            self.tn.write(b'exit\n')
        except:
            log.debug("Error closing connection")
        ##self.disconnect()
        self.tn.close()
        return True


    def request(self,msg):
        self.__init__()
        self.connect()
        if self.write(msg) == True :
            self.close()
            resp = self.read_all()
            return resp
        else :
            return False
