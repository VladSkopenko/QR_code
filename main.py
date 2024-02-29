import qrcode

linka = "https://github.com/VladSkopenko"
img = qrcode.make(linka)
img.save("my_qr_code.png")
