# ECEN5053-002 Embedded Interface Design
# Project 3
* AWS with Graphical Client

### Aakash Kumar/ Hari Srinivas

## Installation Instructions 
* Clone github repository from https://github.com/aakashpk/ecen5053-002-Proj3
* The project uses sendgrid for emailing/messaging of alerts Install sendgrid python API using pip by running `pip3 install sendgrid`
* Uses tinydb as the database, can be installed by running `pip3 install tinydb` 
* Uses boto3 AWS Python SDK , can be installed by running `pip3 install boto3`
* Uses matplotlib for plotting graphs , can be installed by running `pip3 install matplotlib`

### Run Instructions
* run `python3 basicPubSub.py` to start the data publish to AWS
* run `python3 local.py` to start the sensor pi QT interface
* run `python3 client.py` to start the remote pi QT interface showing the graph of data retrived from SQS queue 


### Files in the directory
* basicPubSub.py reads data from the temperature sensor and publishes to AWS 
* sensorRead.py - hardware interface functions, reads values from the DHT sensor and GPIO setup, also takes care of unit conversion between degC and degF
* databaseOps.py - database operations
* window_template.py - QT UI template file
* local.py - qt GUI program to display data
* lambda_code.js - AWS lambda code for getting data from 
* client.py - remote pi QT UI that gets data from SQS queue and plots graph  

## Project Work 
* Aakash Kumar - AWS data publish, AWS lambda rule
* Hari Srinivas - AWS data subscription and graph display in QT UI


## Extra Credit
* SMS Alerts using AWS SNS on High and Low Temperature
* SMS Alerts using AWS SNS on High and Low Humidity
* SMS Alert on sensor disconnection - this is differentiated from the high or low alarm
* Led Alert on sensor disconnection
* Buzzer Sounding on High Temperature


## References
* http://www.fhilitski.com/2016/11/temperature-sensor-with-raspberry-pi-3-and-aws/  help with AWS data push
* base code for AWS data push from AWS sample code
* http://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html AWS help to setup IOT rule, and other AWS documentation pages
* http://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples-send-receive-messages.html
* http://www.codexpedia.com/node-js/amazon-simple-queue-service-sqs-example-in-node-js/
