# QR-Code-Reader-and-Generator
#### Welcome to QRcode Generator and Reader’s documentation! Here, I shall give an overview of all the steps you need to know to get started with this project.

![QR](https://user-images.githubusercontent.com/76250835/102737004-4ea69100-436c-11eb-89cb-8aa2986587e7.png)


This mini project is divided in two parts. i.e., Qrcode Generator and Qrcode Reader respectively.

## Technical Stack
* Pyzbar(Python)
* Qrcode(Python)
* PIL(pillow-Python)
* Webbrowser(Python)

## Installing required Plugins
#### The installation procedure is written keeping command prompt as the base. However you can install the given plugins in any distribution.

Run the given command in command prompt to install pyzbar 
#### pip install pyzbar

Run the given command in command prompt to install pyqrcode
#### pip install PyQRCode

Run the given command in command prompt to install pillow
#### pip install pillow

Run the given command in command prompt to install webbrowser
#### python -m webbrowser


As of now, this project runs on Python 3.x . Make sure that all the given should be installed in any of your python distributions.

## Steps to generate Qrcode
#### First open your IDE and activate the virtual environment in which all the plugins are installed

* To generate the Qr code open the QR Code Generator folder and then open the Generator.py file. Change the link to the link of your website or type your message and run the python file.
* Make sure you change the path of the directory in which you want to save the png image of qrcode. In case of saving the image in the current directory, just specify the name of image within the quotes.  


## Steps to read Qrcode
#### First open your IDE and activate the virtual environment in which all the plugins are installed

* To read the Qr code open the QR Code Reader folder and then the Reader.py file.
* Now run the file

## References
-[PyPi: Qrcode](https://pypi.org/project/PyQRCode/)

-[PyPi: Pyzbar](https://pypi.org/project/pyzbar/)
