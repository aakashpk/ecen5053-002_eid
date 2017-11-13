# ecen5053-002-Proj3
* AWS with Graphical Client

### Aakash Kumar/ Hari Srinivas

##Installation Instructions 
* Clone github repository from https://github.com/aakashpk/ecen5053-002-Proj3
* The project uses sendgrid for emailing/messaging of alerts Install sendgrid python API using pip by running

* pip3 install sendgrid

* Uses tinydb as the database, can be installed by running 

* pip3 install tinydb 

### Run Instructions
* run `python3 basicPubSub.py` to start the data publish to AWS
* run `python3 local.py` to start the sensor pi QT interface
* run `client.py` to start the remote pi QT interface showing the graph of data retrived from SQS queue 


### Files in the directory
* basicPubSub.py reads data from the temperature sensor and publishes to AWS 
* sensorRead.py - hardware interface functions, reads values from the DHT sensor and GPIO setup, also takes care of unit conversion between degC and degF
* databaseOps.py - database operations
* window_template.py - QT UI template file
* local.py - qt GUI program to display data
* lambda_code.js - AWS lambda code for getting data from 
* client.py - remote pi QT UI that gets data from SQS queue and plots graph  

##Project Work 
* Aakash Kumar - AWS data publish, AWS lambda rule
* Hari Srinivas - AWS data subscription and graph display in QT UI


## Extra Credit
* SMS Alerts using AWS SNS on High and Low Temperature
* SMS Alerts using AWS SNS on High and Low Humidity
* SMS Alert on sensor disconnection - this is differentiated from the high or low alarm



## Requirements

## Sensor RPi
* All the stuff from project 2
* Connect to AWS and send data to AWS once every 5 seconds via MQTT


## AWS
* Node.js lambda function that receives incoming lambda function and creates an 8 value message with the latest value, average, max, min of
 the received values. Function should drop the 8 value message on an AWS SQS Queue. 
* This may require creating another SQS queue to retain earlier values to calculate the average etc, as disucssed in 30 Oct class.


## Client RPI
* Web or QT UI that has a request button. When pressed it should retrive the last 30(or less messages ) from the SQS queue. 
 Indicate progress/failure of retrival
* Create 2 graphs on client end, to show values, averages, minimums and maximums of the temp and humidity
* Graph should have no of data items retrived, start and end timestamps of the messages.
* Button to change units between degF and degC
* Possibility of using tkinter or others for the UI application. 


