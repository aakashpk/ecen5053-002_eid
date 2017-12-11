# ecen5053-002-Proj4

## Aakash Kumar/ Hari Shreenivash

### Extra Credit Work
* AMQP protocol using Rabbit MQ


### Install Instuctions
* `pip3 install AWSIoTPythonSDK`
* `pip3 install boto3`
* `pip3 install aiocoap`
* `pip3 install linkheader`
* `pip3 install tornado`
* `pip3 install pika`
* `sudo apt-get install rabbitmq-server`
* 

### Run Instructions
#### On Server
* Start sending data to AWS by running `python3 publishToAWS.py`
* Start mqtt loopback of messages using AWS by running `python3 mqttLoopback`
* Start coap server by running python3 `server_coap.py`
* Start websocket server by running `python3 ws_server`
* Start loopback of AMQP messages by running`python3 amqp_receive.py`
* Run `python3 local_QT_GUI.py` if Server UI is to be viewed

#### On Client
* Run `python3 QT.py` to start the client UI


Rabbit MQ broker is run on the workstation, Start Rabbit MQ broker by running `sudo rabbitmq-server start`

### Files 
#### Server
* amqp_receive.py - amqp message loopback 
* databaseOps.py - functions to create and add data to server databaseOps
* local_QT_GUI.py - server GUI
* mqttLoopback.py - MQTT message loopback 
* publishToAws.py - Functions to setup connection and Publish temperature , humidity data to AWS
* sensorRead.py - sensor interface functions 
* server_coap.py - coap server implementation using aiocoap
* window_template.py - QT GUI template
* ws_server.py - websocket server using tornado

#### Client 
* amqp_send.py - Functions to send and receive AMQP messages and calculate loop time
* client_coap.py - CoAP client implementation using aiocoap , and functions to calculate loop time
* mqttcalc.py -  MQTT message publish, subscribe and functions to calculate loop time
* QT.py - Client GUI
* sqs_pull.py - functions to connect to AWS and pull data from SQS
* ws_client.py - Websocket client using torando and functions to calculate loop time

### Project Work
#### Aakash Kumar
* MQTT
* CoAP
* AMQP

#### Hari Shreenivash
* Websockets
* Qt GUI

#### Refferences
* aiocoap usage http://aiocoap.readthedocs.io/en/latest/examples.html
* websocket client in python http://code.activestate.com/recipes/579076-simple-web-socket-client-implementation-using-torn/
* Rabbit MQ documetation https://www.rabbitmq.com/tutorials/tutorial-one-python.html
* rabbit MQ command line documentation https://www.rabbitmq.com/rabbitmqctl.8.html
* Pika documentation https://pika.readthedocs.io/en/latest/modules/parameters.html

