#Prudhvi Srinivas

#This code encodes a given url or information in a qrcode


import qrcode
import PIL
from PIL import Image

qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)

# You can add a text or a file depending upon your requirement
# Ex:  data="This is my LinkedIn address"

data="https://www.linkedin.com/in/imthe-ps/"
# I added the link of my LinkedIn profile...   :-)

qr.add_data(data)
qr.make(fit=True)

#Choosing the foreground and background color of the qrcode generated
img=qr.make_image(fill_color="black", back_color="white")


#Change the image name as per your requirement
img.save(r'D:\QR\linkedin_link.png')
#Hint :Place the path of the directory in which you wamt to save the image along with its name.

#Uncomment the below line to save the image in the same directory as this python file.
#img.save('profile_qr.png')
