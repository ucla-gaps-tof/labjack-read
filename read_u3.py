import u3
import u6

serial = [320091553,320096837,320091728,320096852] #Serial numbers of four U3 labjacks

for j in range(4):
    d = u3.U3(autoOpen = False)
    d.open(serial = serial[j]) #Connect multiple U3 labjacks
    d.configIO(FIOAnalog=255, EIOAnalog=255) #Set all pins to analog
    d.getCalibrationData()

    print("Labjack " + str(j) + " (" + str(serial[j]) + "):")
    for i in range(16):
        v = round(d.getAIN(i),3)
        if -0.5  < v < 0.5:
            v = 0 #Ignore small inaccuracies in measurement for voltages near zero
        print("   Channel " + str(i) + " voltage: " + str(v))

d = u6.U6()
d.getCalibrationData()
print("Labjack 4 (U6):")
for i in range(16):
    v = d.getAIN(i)
    if -0.5  < v < 0.5:
        v = 0 #Ignore small inaccuracies in measurement for voltages around zero
    print("   Channel " + str(i) + " voltage: " + str(v))