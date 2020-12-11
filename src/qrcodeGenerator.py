# qrcodeGenerator.py: Simple QR Code generator
#
# Project: https://github.com/tamagusko/qrcode
# License: MIT (c) 2020, Tiago Tamagusko
# Author: Tiago Tamagusko <tamagusko@gmail.com>
# Version: 0.3 (2020-12-11)

import qrcode


def qrcodeGenerator(url, filename):
    img = qrcode.make(url)
    img.save(filename)
    return img


url = 'google.com'
filename = 'qrcode.png'

qrcodeGenerator(url, filename)
