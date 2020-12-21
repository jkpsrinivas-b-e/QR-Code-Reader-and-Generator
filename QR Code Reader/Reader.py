#Prudhvi Srinivas

#This code decodes the given Qrcode and opens the website cooresponding to it.

#pyzbar is the alternative to opencv for this mini project
from pyzbar.pyzbar import decode

# pillow is a package in python
# To load the image, we simply import the image module from the pillow and call the Image.
from PIL import Image 


#webbrowser is a python module, which allows to open the web browser from python script.
import webbrowser 


#replace the path in quotes with the path to your png image along with the name of png image.
d=decode(Image.open(r'D:\QR\linkedin_link.png'))


# Saving the decoded in url
url=(d[0].data.decode())
webbrowser.open(url)
#Hurray the url opens a website :-) 
# My LinkedIn profile

#While displaying a simple message encoded in qrcode comment the line 18 and uncomment line 22:
#print(url)
