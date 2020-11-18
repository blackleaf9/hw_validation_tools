# -*- coding: utf-8 -*-
import visa
import time

# E-Load
class BK8600:
	# Initialize to the bay's BK8600 address through USB
	def __init__(self, resource_id='USB0::65535::34816::602197010707510034::0::INSTR'):
		rm = visa.ResourceManager()
		self.inst = rm.open_resource(resource_id)
		print("Connected to %s\n" % self.inst.query("*IDN?"))
		self.inst.write("*RST")

	# To Set E-Load in Amps 
	def set_current(self, current_setpoint_A):		
		self.inst.write("CURR:LEV %s" % current_setpoint_A)
		OPC = self.inst.query("*OPC?")
		self.inst.write("INPut ON")
		return OPC
	
	def set_voltage(self, voltage_setpoint_A):		
		self.inst.write("VOLT:LEV %s" % voltage_setpoint_A)
		OPC = self.inst.query("*OPC?")
		self.inst.write("INPut ON")
		return OPC
		
	def set_resistance(self, resistance_setpoint_A):		
		self.inst.write("RES:LEV %s" % resistance_setpoint_A)
		OPC = self.inst.query("*OPC?")
		self.inst.write("INPut ON")
		return OPC

	def set_power(self, power_setpoint_A):		
		self.inst.write("POW:LEV %s" % power_setpoint_A)
		OPC = self.inst.query("*OPC?")
		self.inst.write("INPut ON")
		return OPC

	def measure_voltage(self):
		return float(self.inst.query("MEAS:VOLT:DC?"))

	def measure_current(self):
		return float(self.inst.query("MEAS:CURR:DC?"))


class DMM_34410A:
	def __init__(self, resource_id = 'USB0::2391::1543::MY47018348::0::INSTR'):
		rm = visa.ResourceManager()
		self.inst = rm.open_resource(resource_id)
		print("Connected to %s\n" % self.inst.query("*IDN?"))
		self.inst.write("*RST")

	def measure_voltage(self):
		return float(self.inst.query("MEAS:VOLT?"))

	def measure_current(self):
		return float(self.inst.query("MEAS:CURR?"))

class E3631A:
	def __init__(self, resource_id = 'ASRL6::INSTR'):
		rm = visa.ResourceManager()
		self.inst = rm.open_resource(resource_id, query_delay=0.5)
		self.inst.baud_rate = 9600
		print("Connected to %s\n" % self.inst.query("*IDN?"))
		self.inst.write("SYST:REM")
		time.sleep(0.1)
		self.inst.write("*RST")

	def measure_voltage(self, output="P25V"):
		time.sleep(0.75)
		self.inst.write(":MEAS:VOLT:DC? %s" % output)
		time.sleep(0.3)
		self.inst.write("*OPC")
		return float(self.inst.read())

	def measure_current(self, output="P25V"):
		time.sleep(0.75)
		self.inst.write(":MEAS:CURR:DC? %s" % output)
		time.sleep(0.3)
		self.inst.write("*OPC")
		return float(self.inst.read())
		#return self.inst.query(":MEASure:VOLTage:DC? P25V")

	def set_output(self, output = "P25V", voltage = 0, current = 0):
		#query = "APPL %s, %s, %s" % (output, voltage, current)
		self.inst.query(("APPL %s, %s, %s") % (output, voltage, current))
	
	def set_current(self, current_setpoint_A):		
		self.inst.write("CURR:LEV %s" % current_setpoint_A)
		OPC = self.inst.query("*OPC?")
		return OPC
	
	def set_voltage(self, voltage_setpoint_A):		
		self.inst.write("VOLT:LEV %s" % voltage_setpoint_A)
		OPC = self.inst.query("*OPC?")
		return OPC

	def output_on(self):
		self.inst.write("OUTP ON")

	def output_off(self):
		self.inst.write("OUTP OFF")

	def close(self):
		self.inst.write("SYST:LOC")

class N8740A:
	def __init__(self, resource_id = ''):
		rm = visa.ResourceManager()
		self.inst = rm.open_resource(resource_id)
		print("Connected to %s\n" % self.inst.query("*IDN?"))
		self.inst.write("*RST")

	def measure_voltage(self):
		return float(self.inst.query("MEAS:VOLT:DC?"))

	def measure_current(self):
		return float(self.inst.query("MEAS:CURR:DC?"))

	def set_output(self, voltage = 0, current = 0):
		if (voltage > 150) or (voltage < 0):
			print ("Voltage Set Point Out of Range\n")
			return False	

		# set current limitß
		self.inst.write("SOUR:CURR:IMM %s" % (current))
		#self.inst.write("SOURce:CURRent:TRIG %s" % (current))

		# set current protection
		self.inst.write("SOUR:CURR:PROT:STAT ON")
		state = str(self.inst.query("SOUR:CURR:PROT:STAT?"))
		if state == 'ON':
			# set voltage level
			self.inst.write("SOUR:VOLT:IMM %s" % (voltage))
			return self.inst.query("SOUR:VOLT:IMM?")
			#self.inst.write("SOURce:VOLTage:TRIG %s" % (voltage))
			#self.inst.write("SOURce:VOLTage:TRIG?")
	
	def output_off(self):
		self.inst.write("OUTP OFF")

	def output_on(self):
		self.inst.write("OUTP ON")

	def close(self):
		self.inst.write("SYST:LOC")

	

if __name__ == "__main__":
	psu = E3631A()
	psu.set_output(output="P6V", voltage=1, current=0.1)
	psu.set_output(output="P25V", voltage = 12, current=0.1)
	psu.output_on()
	#print psu.measure_voltage()
	#print psu.measure_current()
	#psu.close()
	#print psu.measure_voltage()
	#eload = BK8600()
	#eload.set_current(0.1)
	#eload.toggle_eload(True)
	#print eload.measure_voltage()
	#print eload.measure_current()

	#dmm = DMM_34410A()
	#print dmm.measure_voltage()