# ecen5053-002-Proj4

## Aakash Kumar/ Hari Shreenivash

### Install Instuctions
* `pip install AWSIoTPythonSDK`
* `pip install boto3`
* `pip install aiocoap`
* `pip install linkheader`
* `pip install tornado`
* `pip install pika`
* `sudo apt-get install rabbitmq-server`


### Run Instructions
#### On Server
* Start sending data to AWS by running publishtoAWS
* Start mqtt loopback of messages using AWS by running mqttloopback
* Start coap server by running coap server
* Start websocket server by running websocket server
* Start Rabbit MQ broker by running sudo rabbitmq-server start
* Run local qt gui if display required

### Extra Credit
* AMQP protocol using Rabbit MQ

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

cd /mnt/d/UCBoulder/Acads/Sem_1/5053-002_Embedded_interface_design/Projects/Proj4/ecen5053-002-Proj4/
