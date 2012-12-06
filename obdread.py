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
	RPM=(ser.read(4))
	f.write(str(RPM))
	f.write(",")

	ser.write("010D1\r\n")
	SPEED=(ser.read(3))
	f.write(str(SPEED))
	f.write(",")
	
	f.close()
	time.sleep(2)
ser.close()



