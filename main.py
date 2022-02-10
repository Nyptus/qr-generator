import qrcode


def qrgenerator(user_input, version, fill_color, back_color, box_size, border):
    version = int(version)
    # ERROR_CORRECT_L About 7% or less errors can be corrected.
    # ERROR_CORRECT_M (default) About 15%
    # ERROR_CORRECT_Q About 25% or less
    # ERROR_CORRECT_H About 30% or less
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(user_input)
    qr.make(fit=True)
    img = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    )
    img.save(f"{user_input}-{version}-{fill_color}-and-{back_color}-{box_size}-{border}.png")


def main():
    user_input = input("Please enter Your text for QR-code: ")
    user_input_version = input("Please enter 'version' from 1 to 40 (smallest - 1 (21x21): ")
    user_input_fill_color = input("Please enter fill color (white, black, blue, red etc): ")
    user_input_back_color = input("Please enter back color (white, black, blue, red etc): ")
    user_input_box_size = input("Please enter many pixels each “box” of the QR code (10, 14 etc): ")
    user_input_border = input("Please how many boxes thick the border should be: ")
    qrgenerator(
        user_input=user_input,
        version=user_input_version,
        fill_color=user_input_fill_color,
        back_color=user_input_back_color,
        box_size=user_input_box_size,
        border=user_input_border,
    )


if __name__ == "__main__":
    main()
