import pyvisa
import time
from src.equipments.rigol import DS1054Z

#initialize instrument
inst = DS1054Z()

print("Setting up Inst")
inst.setup_channel()
inst.autoscale()

Operation = "ON"
while Operation != "End":
    Operation = input("Enter:\n"+"SC for screen capture\n"+"V to meausre rms voltage\n" + "f to measure frequency\n"+"P to measure period\n"+" End to close testing") 
    if Operation == "SC":
        inst.screencapture()
    elif Operation == "V":
        print("rms voltage is: %d", inst.measure_rmsvoltage())

    elif Operation == 'f':

        print("frequency is: %d", inst.frequency())

    elif Operation == 'p':
        print("frequency is: %d", inst.period())

    elif Operation == 'End':
        print("frequency is: %d", inst.period())
        print("Manual Testing Done")
    else :
        print("Error")
        time.sleep(2)


print("Manual Testing Done")

