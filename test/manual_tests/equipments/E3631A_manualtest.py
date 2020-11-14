import pyvisa
import time
from src.equipments.lab_equipment import E3631A

TEST_OUTPUT = "P25V"
TIME = 10



#initialize instrument
inst = E3631A()
# To Set Output
inst.set_output(TEST_OUTPUT,0,0)
print("Output set at " + TEST_OUTPUT)
time.sleep(5)
Operation = "OFF"

while(Operation == "OFF"):
    Operation = input("Enter ON to turn on Output")
    if Operation == "ON":
        inst.output_on()
        print("Output On")
    time.sleep(10)

while Operation != "End":
    Operation = input("Enter:\n"+ "V to measure Voltage\n" + "C to measure Current\n" +"OFF to turn output off\n"+"End to close testing") 
    if Operation == 'C':
        print("Measuring Current")
        time.sleep(2)
        print("current is: %d", inst.measure_current())
        time.sleep(10)
        
    elif Operation == 'V':  
        print("Measuring Voltage")
        time.sleep(2) 
        print("voltage is: %d", inst.measure_voltage())
        time.sleep(10)
    
    elif Operation == 'OFF':
        inst.output_off() 
        print("Output OFF")
        time.sleep(10)
        while(Operation != "ON"):
            Operation = input("Enter ON to turn on Output")
            if Operation == "ON":
                inst.output_on()
                print("Output On")
                time.sleep(10)
    
    else :
        print("Error")
        time.sleep(2)

inst.output_off() 
time.sleep(1)
inst.close()
print("Manual Testing Done")


