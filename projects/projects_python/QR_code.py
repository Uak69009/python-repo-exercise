import qrcode
from PIL import Image
qr = qrcode.QRCode ( 
    version = 15,
    box_size = 10,
    border = 5
)

data = 'https://www.instagram.com/umairamjadkhanyousafzai/'

img = qr.make_image(fill='black', back_color='white')
img.save("instagram_qr.png")