import pyvisa
import time
from src.equipments.lab_equipment import N8740A

TIME = 2


Operation = "OFF"
#initialize instrument
while(Operation == "OFF"):
    Operation = input("Enter ON to turn on Output")
    if Operation == "ON":
        inst = N8740A()
        print("Output On")
    time.sleep(0.2)

print("Set Output")
voltage = input("Enter Output Voltage")
current = input("Enter Output Current")
inst.set_output(voltage,current)
print("Output Set")


while Operation != "End":
    Operation = input("Enter:\n"+ "V to measure Voltage\n" + "C to measure Current\n" +"OFF to turn output off\n"+"End to close testing") 
    if Operation == 'C':
        print("Measuring Current")
        time.sleep(0.2)
        print("current is: %d", inst.measure_current())
        time.sleep(0.2)
        
    elif Operation == 'V':  
        print("Measuring Voltage")
        time.sleep(0.2) 
        print("voltage is: %d", inst.measure_voltage())
        time.sleep(0.2)
    
    elif Operation == 'OFF':
        inst.output_off() 
        print("Output OFF")
        time.sleep(0.2)
        while(Operation != "ON"):
            Operation = input("Enter ON to turn on Output")
            if Operation == "ON":
                voltage = input("Enter Output Voltage")
                current = input("Enter Output Current")
                inst.set_output(voltage,current)
                inst.output_on()
                print("Output On")
                time.sleep(1)

    elif Operation == 'End':
        inst.output_off() 
        time.sleep(0.2)
        inst.close()
        print("Manual Testing Done")
    else :
        print("Error")
        time.sleep(0.2)

