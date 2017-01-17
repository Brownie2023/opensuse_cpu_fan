'''
Program: OpenSuse-MBP-FanControl
Version: 0.1
Description: This is a simple script that checks the current CPU temperature every 5 seconds
             and adjusts the fan speed accordingly.
Author: Josh Brown
Date: 1.1.17
Python Version: 3
'''

#!/usr/bin/python3

import sys, time

if __name__ == "__main__":
    while True:
        temperature_file = open('/sys/class/thermal/thermal_zone1/temp', encoding='utf-8')
        cpu_tmp_string = temperature_file.read()
        temperature_file.close()
        cpu_tmp = int(cpu_tmp_string) / 1000
        fanspeed_file_1 = open('/sys/devices/platform/applesmc.768/fan1_min', 'w')
        fanspeed_file_2 = open('/sys/devices/platform/applesmc.768/fan2_min', 'w')
        if cpu_tmp > 79:
            fanspeed_file_1.write('6000')
            fanspeed_file_2.write('6000')
        elif cpu_tmp > 73:
            fanspeed_file_1.write('5000')
            fanspeed_file_2.write('5000')
        else:
            fanspeed_file_1.write('4000')
            fanspeed_file_2.write('4000')
        fanspeed_file_1.close()
        fanspeed_file_2.close()
        print("CPU TEMP: " + str(cpu_tmp), end='\r')
        time.sleep(5)
