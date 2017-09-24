
#!/usr/bin/python

from sense_hat import SenseHat
import time, os, sys

sense = SenseHat()
sense.clear()
sense.low_light = True

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

try:

      while True:

            now = time.strftime("%S")

            if  float(now)==0:

                sense.clear()
                current_time = time.strftime("%H:%M")
                print("Current Time",current_time)

                cpu_temp = getCPUtemperature()
                temp = sense.get_temperature()
                temp_p = sense.get_temperature_from_pressure()
                temp_cal = float(temp) - (float(cpu_temp)-float(temp))/3.037
                temp = round(temp, 1)
                cpu_temp = round(float(cpu_temp), 1)
                temp_p = round(temp_p, 1)
                temp_cal = round(temp_cal, 1)

                print("Temperature Sense",temp)
                print("Temperature P",temp_p)
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

            else:
                yellow = (255, 255, 102)
                blue = (135, 206, 235)
                
                sense.set_pixel(1, 2, yellow)
                sense.set_pixel(2, 1, yellow)
                sense.set_pixel(3, 2, yellow) 
                sense.set_pixel(4, 2, yellow)
                sense.set_pixel(5, 1, yellow)
                sense.set_pixel(6, 2, yellow)
                
                sense.set_pixel(0, 3, yellow)
                sense.set_pixel(0, 4, yellow)
                sense.set_pixel(0, 5, yellow)
                sense.set_pixel(1, 6, yellow)
                sense.set_pixel(2, 7, yellow)
                sense.set_pixel(3, 7, yellow)
                sense.set_pixel(4, 7, yellow)
                sense.set_pixel(5, 7, yellow)
                sense.set_pixel(6, 6, yellow)
                sense.set_pixel(7, 5, yellow)
                sense.set_pixel(7, 4, yellow)
                sense.set_pixel(7, 3, yellow)
                
                sense.set_pixel(2, 4, blue)
                sense.set_pixel(5, 4, blue)
                
                time.sleep(0.5)

except KeyboardInterrupt:
      pass

sense.clear()
