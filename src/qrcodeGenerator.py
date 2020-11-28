# File: src/qrcodeGenerator.py
#   Simple QR Code generator
#
# Project page: https://github.com/tamagusko/qrcode
# License: MIT - Copyright 2020 Tiago Tamagusko
# Author: Tiago Tamagusko <tamagusko@gmail.com>
# Version: 0.1 (2020-11-28)

import qrcode


def qrcodeGenerator(url, filename='qrcode.png'):
    img = qrcode.make(url)
    img.save(filename)
    return img


url = 'https://www.jest.pt'
filename = 'qrcode.png'
qrcodeGenerator(url, filename)
