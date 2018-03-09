import sys
import yaml
import requests
import calendar
import time
from time import gmtime, strftime
from datetime import datetime
from pyfoobot import Foobot

def round_down(num, divisor):
    return num - (num%divisor)

if len(sys.argv) != 2:
	print "python yesterday.py <config.yaml>"
	exit()
config_file = sys.argv[1]

with open(config_file, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
apikey=cfg['foobot']['apikey'][-24:]
email=cfg['foobot']['email']
password=cfg['foobot']['password']
print("apikey=",apikey)
print("email=",email)
print("password=",password)
"""
fb = Foobot(apikey, email, password)
devices = fb.devices()
print("devices=",devices)

# Devices is a list, in case you have more than one foobot
device = devices[0]
print("device=",device)

# Get the most recent sample
#latest_data = device.latest()
#print("latest_data=",latest_data)

# Get data from the last hour
#last_hour_data = device.data_period(3600, 600)
#print("last_hour_data=",last_hour_data)

# Get data for a data range
range_data = device.data_range(start='1520208000',
                               end='1520211600',
                               sampling=0)
"""
range_data= {u'end':1520208549, u'uuid':u'25004664144000A1', u'start':1520208244, 
u'datapoints': [[1520208244, 10.880005, 18.651, 45.771, 571, 159, 15.737148], 
[1520208549, 10.880005, 18.684, 45.649, 563, 156, 15.308577]], 
u'units': [u's', u'ugm3', u'C', u'pc', u'ppm', u'ppb', u'%'], 
u'sensors': [u'time', u'pm', u'tmp', u'hum', u'co2', u'voc', u'allpollu']}

print("range_data=",range_data)          
print("start=",range_data['start'])
print("end=",range_data['end'])
print("uuid=",range_data['uuid'])                     
print("datapoints=",range_data['datapoints'])
print("datapoints[0][0]=",range_data['datapoints'][0][0])
print("units=",range_data['units'])
print("sensors=",range_data['sensors'])
print("sensors[0]=",range_data['sensors'][0])

units=dict()
for pos in range(len(range_data['sensors'])):
	units[range_data['sensors'][pos]]=range_data['units'][pos]
if(units['tmp']!='C'):
	print("Temperature must be in C to graph")
	exit()

sensor_data=dict()
for datapoints in range_data['datapoints']:
	sd=dict()
	print("------------------------------------------")
	print("datapoints=",datapoints)
	for pos in range(len(range_data['sensors'])):
		sd[range_data['sensors'][pos]]=datapoints[pos]
	unixtime = time.gmtime(sd['time'])
	round_time=datetime(unixtime.tm_year,unixtime.tm_mon,unixtime.tm_mday,unixtime.tm_hour,round_down(unixtime.tm_min,10),0).strftime('%s')
	
	print(strftime("%a, %d %b %Y %H:%M:%S +0000", unixtime))
	print("unixtime=",unixtime)
	print("roundtime=",round_time)
	#print("roundtime2=",strftime("%a, %d %b %Y %H:%M:%S +0000", datetime.timetuple(round_time)))
	if round_time not in sensor_data:
		sensor_data[round_time]=sd

print("------------------------------------------")
tt = datetime.timetuple(datetime(1970, 1, 1, 0, 0, 0))
print("tt=",tt)
print(strftime("%a, %d %b %Y %H:%M:%S +0000", tt))
print("sensor_data=",sensor_data)	

# ---------------------------------------------------------------------- REQUESTS
#for reading in sensor_data:
for unix_time, readings in sensor_data.iteritems():
	print("unix_time=",unix_time)
	print("tmp=",readings['tmp'])
	url = 'http://localhost/iaq/get_reading.php?unix_time={}&temp={}&hum={}&hcho=&sewer={}&dust={}&core_id={}&uptime={}' \
      .format(unix_time, readings['tmp'], readings['hum'], readings['voc'], readings['pm'], apikey, 0)
	print(url)

	r = requests.get(url)
	#print r.status_code
	#print r.headers
	print("content=",r.content)
