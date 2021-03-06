import random
import os
import time
from ras_data.models import ras_info
import Adafruit_DHT
from w1thermsensor import W1ThermSensor

sensor1 = Adafruit_DHT.DHT11
sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "03059779864b")

def getCPUtemp():
    temp = os.popen('vcgencmd measure_temp').readline()
    tempfloat = float(temp.replace('temp=', '').replace('\'C\n', ''))
    return tempfloat


def getCPUusage():
    # calculate CPU with two short time, time2 - time1
    time1 = os.popen('cat /proc/stat').readline().split()[1:5]
    time.sleep(0.2)
    time2 = os.popen('cat /proc/stat').readline().split()[1:5]
    deltaUsed = int(time2[0]) - int(time1[0]) + int(time2[2]) - int(time1[2])
    deltaTotal = deltaUsed + int(time2[3]) - int(time1[3])
    cpuUsage = float(deltaUsed) / float(deltaTotal) * 100
    return cpuUsage

def getRAM():
    # get RAM as list,list[7],[8],[9]:total,used,free
    RAM = os.popen('free').read().split()[7:10]
    # convert kb in Mb for readablility
    RAM0 = float(RAM[0]) / 1024
    RAM1 = float(RAM[1]) / 1024
    percent = RAM1 / RAM0 * 100
    RAM2 = float(RAM[2]) / 1024
    return [RAM0,RAM1,RAM2,percent]

def getDisk():
    # get Disk information,DISK[8],[9],[10],[11]:Size, Used. free, Used %
    DISK = os.popen('df -h /').read().split()[8:12]
    # print
    # 'Disk total space is %s ' % DISK[0]
    # print
    # 'Disk Used  space is %s ' % DISK[1] + 'and is %s' % DISK[3]
    # print
    # 'Disk Free  space is %s ' % DISK[2]
    return DISK

def get_data():
    data = ras_info()
    humidity, temperature = Adafruit_DHT.read_retry(sensor1, 26)
    temperature = sensor2.get_temperature()
    data.T = temperature
    data.H = humidity
    try:
        data.CT = getCPUtemp()
    except:
        data.CT = random.uniform(10, 80)

    try:
        data.CU = getCPUusage()
    except:
        data.CU = random.uniform(10, 80)

    try:
        disk = getDisk()
        data.DT = float(disk[0][0:-1])
        data.DU = float(disk[1][0:-1])
        data.DF = float(disk[2][0:-1])
        data.DP = float(disk[3][0:-1])
    except:
        data.DT = random.uniform(10, 80)
        data.DU = random.uniform(10, 80)
        data.DF = random.uniform(10, 80)
        data.DP = random.uniform(10, 80)

    try:
        ram = getRAM()
        data.RT = ram[0]
        data.RU = ram[1]
        data.RF = ram[2]
        data.RP = ram[3]
    except:
        data.RT = random.uniform(10, 80)
        data.RU = random.uniform(10, 80)
        data.RF = random.uniform(10, 80)
        data.RP = random.uniform(10, 80)
    data.save()

