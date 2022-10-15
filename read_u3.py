import u3
import u6

serial = [320091553,320096837,320091728,320096852] #Serial numbers of four U3 labjacks
id = ["AIN","EIO"]

def loadu3(ljstart):
    d = u3.U3(autoOpen = False)
    d.open(serial = serial[j + ljstart]) #Connect multiple U3 labjacks
    d.configIO(FIOAnalog=255, EIOAnalog=255) #Set all pins to analog
    d.getCalibrationData()
    print("Labjack " + str(j) + " (U3) (" + str(serial[j + ljstart]) + "):")

def read(ljstart,ljrange,index):
    for i in range(ljrange):
        v = round(d.getAIN(i+ljstart),3)
        print("   " + id[index] + " " + str(i+ljstart) + ": " + str(v) + " V")

for j in range(2):
    loadu3(0)
    read(0,4,0)
    read(8,8,1)

for j in range(2):
    loadu3(2)
    read(0,4,0)

d = u6.U6()
d.getCalibrationData()
print("Labjack 4 (U6):")
read(0,4,0)
read(10,10,1)