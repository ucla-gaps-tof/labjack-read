import u3
import u6

serial = [320091553,320096837,320091728,320096852] #Serial numbers of four U3 labjacks
id = ["AIN","EIO"]

def read(ljstart,ljrange,index,shift):
    for i in range(ljrange):
        v = round(d.getAIN(i+ljstart),3)
        print("   " + id[index] + " " + str(i+shift) + ": " + str(v) + " V")

for j in range(2):
    d = u3.U3(autoOpen = False)
    d.open(serial = serial[j]) #Connect multiple U3 labjacks
    d.configIO(FIOAnalog=255, EIOAnalog=255) #Set all pins to analog
    d.getCalibrationData()
    print("Labjack " + str(j) + " (U3) (" + str(serial[j]) + "):")
    read(0,4,0,0)
    read(8,8,1,0)

for j in range(2):
    d = u3.U3(autoOpen = False)
    d.open(serial = serial[j+2]) #Connect multiple U3 labjacks
    d.configIO(FIOAnalog=255, EIOAnalog=255) #Set all pins to analog
    d.getCalibrationData()
    print("Labjack " + str(j+2) + " (U3) (" + str(serial[j+2]) + "):")
    read(0,4,0,2)

d = u6.U6()
d.getCalibrationData()
print("Labjack 4 (U6):")
read(0,4,0,0)
read(10,10,1,10)