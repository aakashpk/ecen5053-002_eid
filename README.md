# ecen5053-002-Proj3
* AWS with Graphical Client

## Requirements

## /////// Sensor RPi
1 All the stuff from project 2
2 Look into possibility of changinf to redis for database
3 Connect to AWS and send data to AWS once every 5 seconds via MQTT


## ///////// AWS
1 Node.js lambda function that receives incoming lambda function and creates an 8 value message with the latest value, average, max, min of
 the received values. Function should drop the 8 value message on an AWS SQS Queue. 
2 This may require creating another SQS queue to retain earlier values to calculate the average etc, as disucssed in 30 Oct class.


## ///// Client RPI
1 Web or QT UI that has a request button. When pressed it should retrive the last 30(or less messages ) from the SQS queue. 
 Indicate progress/failure of retrival
2 Create 2 graphs on client end, to show values, averages, minimums and maximums of the temp and humidity
3 Graph should have no of data items retrived, start and end timestamps of the messages.
4 Button to change units between degF and degC
5 Possibility of using tkinter or others for the UI application. 


### Files from project2
*index.html - base web page to be displayed
*main.js - javascript/jQuery being used in the webpage
*style.css - css style sheets for the webpage
*server.py - setup of websocket server and database and continuous data update
*sensorRead.py - hardware interface functions, reads values from the DHT sensor and GPIO setup, also takes care of unit conversion between degC and degF
*databaseOps.py - database operations and responses to tornado queries
*window_template.py - QT UI template file
*local.py - qt GUI program to display data