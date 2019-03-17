// Load the AWS SDK
var AWS = require("aws-sdk");

exports.handler = (event, context, callback) => {
   // Load the message passed into the Lambda function into a JSON object 
    var eventText = JSON.stringify(event, null, 2); 
    
    // Log a message to the console, you can view this text in the Monitoring tab in the Lambda console or in the CloudWatch Logs console
    console.log("Received event:", eventText);
    // extracting the 
    var curTs=event.ts;
    
    var curTemp= Number(event.Temperature);
    console.log("curtemp ",curTemp);
    var curHum=Number(event.Humidity);
    console.log("curhum ",curHum);
    
    const SQS = new AWS.SQS({ apiVersion: '2012-11-05' });
    const QUEUE_URL = process.env.queueUrl;
    const LAST_QUEUE_URL = process.env.lastQueueUrl;
    var result="";
    
    var calc_params = {
      QueueUrl: LAST_QUEUE_URL,
      MaxNumberOfMessages: 1
    };
    
    SQS.receiveMessage(calc_params, function(err, data) {
            if (err) {
                console.log("Error", err);
            } else 
            {
                // default 100,0,0,100,0,0,0
                result= data.Messages[0].Body;
                var handle = data.Messages[0].ReceiptHandle
                
                var deleteParams = {
                QueueUrl: LAST_QUEUE_URL,
                ReceiptHandle: handle
                };
                SQS.deleteMessage(deleteParams, function(err, data) {
                if (err) {
                console.log("Delete Error", err);
                } else {
                console.log("Message Deleted", data);
                }
                }); // end of deleteMessage
                
                
                console.log("Succed ", data);
                console.log("Got last Q",result);
                var array = result.split(",");
                console.log("Array ",array);
    
                // get minimum 
                var minTemp
                 if(curTemp<Number(array[0])) minTemp=curTemp;
                 else minTemp=Number(array[0]);
                
                var maxTemp
                if(curTemp>Number(array[2])) maxTemp=curTemp;
                else maxTemp=Number(array[2]);
    
                 var minHum
                if(curHum<Number(array[3])) minHum=curHum;
                else minHum=Number(array[3]);
    
                var maxHum;
                if(curHum>Number(array[5])) maxHum=curHum;
                else maxHum=Number(array[5]);
    
                //get averages by increasing the count from the last value queue 
                //and averaging the current value with it
                var lastCount=Number(array[6]);
                var count=Number(array[6])+1;
                var avgTemp= ((lastCount*Number(array[1]))+curTemp)/count;
                var avgHum=((lastCount*Number(array[4]))+curHum)/count;
    
                var lastQmessage = minTemp+","+avgTemp+","+maxTemp+","+minHum+","+avgHum+","+maxHum+","+count;
                var curQmessage = curTs+","+ curTemp+","+minTemp+","+avgTemp+","+maxTemp+","+curHum+","+minHum+","+avgHum+","+maxHum;
                // Write the string to the console
                console.log("last Queue ",lastQmessage);
                console.log("End result ",curQmessage);
                
                // writing data to current data SQS Q
                var curQparams = {
                MessageBody: curQmessage,
                QueueUrl: QUEUE_URL
                };
    
                SQS.sendMessage(curQparams, function(err, data) {
                if (err) {
                console.log("Error", err);
                } else {
                console.log("Success", data.MessageId);
                }
                 }); 
 
                // writing data to Last Value SQS Q
                var lastQparams = {
                MessageBody: lastQmessage,
                 QueueUrl: LAST_QUEUE_URL
                };
            
                SQS.sendMessage(lastQparams, function(err, data) {
                if (err) {
                console.log("Error", err);
                } else {
                console.log("Success", data.MessageId);
                }
                 });
                
            } // end of else loop
        }); // end of receiveMessage
    
};