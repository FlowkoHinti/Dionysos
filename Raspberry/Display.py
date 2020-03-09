import serial


class display:

    def __init__(self, port, baudrate):
        try:
            self.serialCon = serial.Serial(port, baudrate)
        except:
            print("Couldn't open Serial port")
        self.displayWidth = 0
        self.displayHight = 0
        self.getDisplay()
        print(self.displayWidth)
        print(self.displayHight)

    def getDisplay(self):
        while self.checkSer():
            self.writeSer('SYNACK')
            if b'ACK' in self.serialCon.readline():
                self.displayWidth = int(self.serialCon.readline().decode('utf-8'))
                self.displayHight = int(self.serialCon.readline().decode('utf-8'))
                break

    def writeSer(self, msg):
        self.checkSer()
        try:
            self.serialCon.write(msg.encode('utf-8'))
        except:
            print("Could not write to Serial")

    def readSer(self):
        self.checkSer()
        try:
            rec = self.serialCon.readline()
            print(rec)
            return rec
        except:
            print("Couldn't read Serial")

    def checkSer(self):
        try:
            return self.serialCon.is_open
        except:
            print("Connection lost")

    def closeSer(self):
        try:
            self.serialCon.close()
        except:
            print("Serial could not be closed")


if __name__ == '__main__':
    disp = display('COM3', 19200)
    disp.writeSer('23,3')
    disp.readSer()
    disp.readSer()
