#DHT22 library from Adafruit
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temp = Adafruit_DHT.read_retry(sensor, pin)

temp_f=((temperature*1.8)+32)

if(sys.argv[1]==f)
	temp=temp_f

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temp, humidity))
else:
    print('Failed to get reading. Try again!')