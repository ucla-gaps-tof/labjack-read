import u3
import u6

serial = [320091553,320096837,320091728,320096852] #Serial numbers of four U3 l$
id = ["AIN","EIO"]
R1 = 75
R2 = 2.7

def read(ljstart,ljrange,index,v_in):
    for i in range(ljrange):
        if v_in == 0:
            v = round(d.getAIN(i+ljstart),2)
            print("   " + id[index] + " " + str(i+ljstart) + ": " + str(v) + " V")
        if v_in == 1:
            v = round(d.getAIN(i+ljstart)*(R1+R2)/R2,2)
            print("   " + id[index] + " " + str(i+ljstart) + ": " + str(v) + " V (V_in)")

for j in range(2):
    d = u3.U3(autoOpen = False)
    d.open(serial = serial[j]) #Connect multiple U3 labjacks
    d.configIO(FIOAnalog=255, EIOAnalog=255) #Set all pins to analog
    d.getCalibrationData()

    print("Labjack " + str(j) + " (U3) (" + str(serial[j]) + "):")
    read(0,4,0,0)
    read(8,8,1,1)

for j in range(2):
    d = u3.U3(autoOpen = False)
    d.open(serial = serial[j+2]) #Connect multiple U3 labjacks
    d.configIO(FIOAnalog=255, EIOAnalog=255) #Set all pins to analog
    d.getCalibrationData()

    print("Labjack " + str(j+2) + " (U3) (" + str(serial[j+2]) + "):")
    read(0,4,0,0)

d = u6.U6()
d.getCalibrationData()
print("Labjack 4 (U6):")
read(0,4,0,0)
read(10,10,1,0)
