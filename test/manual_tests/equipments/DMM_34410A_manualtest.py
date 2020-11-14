import pyvisa
import time
from src.equipments.lab_equipment import DMM_34410A

TIME = 2



#initialize instrument
inst = DMM_34410A()
Operation = "ON"
while Operation != "End":
    Operation = input("Enter:\n"+"V to meausre voltage\n" + "C to measure current\n"+" End to close testing") 
    if Operation == "V":
        try:
            while True:
                print("voltage is: %d", inst.measure_voltage())
                time.sleep(2)
        except KeyboardInterrupt:
            pass

    elif Operation == 'C':
        try:
            while True:
                print("current is: %d", inst.measure_current())
                time.sleep(2)
        except KeyboardInterrupt:
            pass
    else :
        print("Error")
        time.sleep(2)


print("Manual Testing Done")



