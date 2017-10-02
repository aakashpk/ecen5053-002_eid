Aakash Kumar

Project 1 of ECEN-5053-002 Embedded Interface Design
Temperature Sensor Interface with Raspberry Pi and UI using QT
Ability to switch between degF and degC values
Auto refresh of values at user defined periods
 
Installation Instructions
Clone github repository from https://github.com/aakashpk/ecen5053-002_Proj1
The project uses sendgrid for emailing/messaging of alerts
Install sendgrid python API using pip by running
pip3 install sendgrid
to view ui run the python file display_data_update.py

Project Work
Aakash Kumar - responsible for all parts

Project Additions

Ability to switch between degC and degF values. A radio button on the screen allows user to choose between degC and degF as units for temperature.

Automatic refresh of temperature reading at a user specified interval. The interval can be set from the settings tab, and changing the Auto Refresh Delay parameter. The save button has to be pressed once the value is updated.

Ability to set a high temperature alarm limit. The high limit for the temperature can be set by changing the Temperature Alarm Limit parameter in the settings tab. Once the temperature exceeds the high limit, the temperature display background changes to red color and an email/text message is sent to inform user about the alarm condition. The email alert is accomplished using sendgrid integration. 


References

http://wiki.qt.io/Raspberry_Pi_Beginners_Guide

https://www.baldengineer.com/raspberry-pi-gui-tutorial.html

http://pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/

https://stackoverflow.com/questions/8600161/executing-periodic-actions-in-python

https://lifehacker.com/5506326/how-can-i-send-an-email-via-text-message

https://www.youtube.com/watch?v=lcPps6lUK8c

https://github.com/sendgrid/sendgrid-python#quick_start 

https://stackoverflow.com/questions/10875274/change-color-of-lcd-digits-in-qt-designer
 
https://www.tutorialspoint.com/pyqt/pyqt_qcombobox_widget.htm

https://www.youtube.com/watch?v=5Lb8DZhAAi8

