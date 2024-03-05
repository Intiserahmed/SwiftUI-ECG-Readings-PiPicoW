
from ble_simple_peripheral import BLESimplePeripheral
import bluetooth
import time
from machine import Pin, ADC
import ujson

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)
adc = ADC(4)

while True:
    if sp.is_connected():  # Check if a BLE connection is established
        # Read the value from the ADC
        ecg_data = adc.read_u16()
        # Get current timestamp
        timestamp = time.time()

        # Create JSON data with ECG reading and timestamp
        data = {"timestamp": timestamp, "ecg_data": ecg_data}
        data_str = ujson.dumps(data)
        sp.send(data_str)

        time.sleep(0.002)  # Delay for 2 milliseconds (1 / 500 Hz)


