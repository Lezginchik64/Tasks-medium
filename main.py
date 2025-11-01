import qrcode
data = "https://vk.com/mpirimova"
qr = qrcode.QRCode()
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
img.save("my_qr.png")