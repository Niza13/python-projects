import qrcode

def generate_qr_code(image_url, qr_code_filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(image_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_code_filename)

if __name__ == "__main__":
    # Replace 'image_url_here' with the actual URL of your image
    image_url = "fish1.png"
    
    # Replace 'qr_code_filename.png' with the desired filename for your QR code image
    qr_code_filename = "qr_code_image.png"

    generate_qr_code(image_url, qr_code_filename)
