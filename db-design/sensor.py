import serial
from serial.tools import list_ports
import sys

#ser = serial.Serial("/dev/cu.usbmodem1102", 115200, timeout=90) # By Manual

ser = serial.Serial()
ser.baudrate = 115200
ser.timeout = 90
ports = list_ports.comports()
devices = [info.device for info in ports]

if len(devices) == 0:
    print("Device not found.")
    exit()
elif len(devices) == 1:
    print("A devices was found.")
    print(devices)
    ser.port = devices[0]
else:
    print("Many devices was found. Select one.")
    for i in range(len(devices)):
        print(str(i) + ":", devices[i])
    ser.port = devices[int(input())]

try:
    ser.open()
except:
    print("error")

ser.flushInput()
ser.flushOutput()

while True:
    try:
        line = ser.readline()
        line = line.strip()
        a = str(line).split(",")
        print(a[0], a[1], a[2])
    except:
        break;

