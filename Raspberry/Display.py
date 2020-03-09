import serial

class display:

    def __init__(self, port, rate):
        self.port = port
        self.rate = rate
        self.displayWidth = 0
        self.displayHight = 0
        display.serialOpen(self)
        print(str(self.displayHight))
        print(str(self.displayWidth))

    def serialOpen(self):
        with serial.Serial('COM3', 19200) as serialCon:
            while serialCon.is_open:
                serialCon.write(b'SYNACK')
                if b'ACK' in serialCon.readline():
                    self.displayWidth = int(serialCon.readline().decode('utf-8'))
                    self.displayHight = int(serialCon.readline().decode('utf-8'))
                    break


if __name__ == '__main__':
    disp = display('COM3', 19200)

