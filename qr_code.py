"""python script to create a qr code"""
# pip install qrcode
# pip install Pillow

import qrcode


class MyQR:
    def __init__(
            self,
            size: int,
            padding: int
    ) -> None:
        self.qr = qrcode.QRCode(
            box_size=size, border=padding
        )

    def create_qr(
            self,
            file_name: str
    ) -> None:
        user_input = input("Enter the text: ")
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color='red', back_color='white')
            qr_image.save(file_name)
            print("QR code generated successfully")
        except Exception as e:
            print(f"Exception occurred while generating the QR code: {e}")

def main() -> None:
    my_qr = MyQR(10, 4)
    my_qr.create_qr('qr_code.png')

if __name__ == '__main__':
    main()
