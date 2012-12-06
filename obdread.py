#
#   Author : Sajin George
#   Company : RIT
#   Dis: read OBDII information and commit store in log file, 
#
import serial
import time
#print("opening Serial\n")
ser= serial.Serial('/dev/ttyUSB0',115200,timeout=1)

#print("testing ATZ\n")
#ser.write("AT I\r\n")
#print("wating for ATZ response\n")
#print(ser.read(10))


while(True):
	f=open("log.txt",'a')
	
	ser.write("010C1\r\n")
	RPM=(ser.read(ser.inWaiting()))
	f.write(str(RPM))
	f.write(",")

	ser.write("010D1\r\n")
	SPEED=(ser.read(ser.inWaiting()))
	f.write(str(SPEED))
	f.write(",")
	
	f.close()
	time.sleep(2)
ser.close()



