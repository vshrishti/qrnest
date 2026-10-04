import qrcode
username = "shrriishhh"
url = f"https://x.com/{username}"
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(
    fill_color="black",
    back_color="white"
)
img.save("twitter_qrcode.png")
print(f"QR code generated successfully: {url}")
