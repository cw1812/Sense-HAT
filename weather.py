
#!/usr/bin/python

from sense_hat import SenseHat
import time, os, sys

sense = SenseHat()
sense.clear()

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

try:

      while True:

            now = time.strftime("%S")

            if  float(now)==0:

                current_time = time.strftime("%H:%M")
                print("Current Time",current_time)

                cpu_temp = getCPUtemperature()
                temp = sense.get_temperature()
                temp_cal = float(temp) - ((float(cpu_temp) - float(temp))/1.5)
                temp = round(temp, 1)
                cpu_temp = round(float(cpu_temp), 1)
                temp_cal = round(temp_cal, 1)

                print("Temperature Sense",temp)
                print("Temperature CPU",cpu_temp)
                print("Temperature Cal",temp_cal)

                humidity = sense.get_humidity()
                humidity = round(humidity, 1)
                print("Humidity RH%",humidity)

                pressure = sense.get_pressure()
                pressure = round(pressure, 1)
                print("Pressure hPa",pressure)

                accelerometer_data = sense.get_accelerometer_raw()
                x = round(accelerometer_data['x'], 0)
                y = round(accelerometer_data['y'], 0)

                if    y == -1:
                      sense.set_rotation(180)
                elif  x == 1:
                      sense.set_rotation(270)
                elif  x == -1:
                      sense.set_rotation(90)
                else:
                      sense.set_rotation(0)

                sense.show_message(current_time + "  " + str(temp_cal) + "C  " + str(humidity) + "%  " + str(pressure) + "hPa  ", scroll_speed=(0.1), back_colour= [0,0,0], text_colour= [200,0,200])

                sense.low_light = True

            else:
                time.sleep(0.5)

except KeyboardInterrupt:
      pass

sense.clear()
