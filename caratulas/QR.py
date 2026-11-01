import qrcode

# URL que deseas convertir en QR
url = "https://forms.gle/AXanZA7hDwuHLk1i8"

# Genera el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crea la imagen del QR
img = qr.make_image(fill='black', back_color='white')

# Guarda la imagen del QR
img.save("qr_code.png")
