#! /usr/bin/env python

from pyqrcode import QRCode
from PIL import Image, ImageDraw, ImageFont

'''
Generates sheets of 10 labels with sequentially numbered
QR codes formatted for printing on Avery 8161 labels.

George S. Williams physicist@websterling.com 07/2018
'''

start = 1000001
num_sheets = 4

count = start - 1

for j in range(1, num_sheets + 1):
    sheet = Image.new('RGBA', (590, 720), (255, 255, 255, 255))

    for i in range(0, 20):
        count = count + 1
        qr = QRCode(count)
        qr.png('qr.png', scale=2)

        qr_img = Image.open('qr.png', 'r')
        qr_img_w, qr_img_h = qr_img.size
        label = Image.new('RGBA', (288, 72), (255, 255, 255, 255))
        bg_w, bg_h = label.size
        offset = ((bg_h - qr_img_h) // 2, (bg_h - qr_img_h) // 2)
        label.paste(qr_img, offset)

        font = ImageFont.load('helvetica-10.pil')
        d = ImageDraw.Draw(label)
        d.text((130, 22), "Field Sample", font=font, fill=(0, 0, 0))
        d.text((138, 37), str(count), font=font, fill=(0, 0, 0))

        h_offset = i % 2 * 302
        row = abs(i / 2)
        y_offset = row * 72
        sheet.paste(label, (h_offset, y_offset))

    sheet_name = 'sheet' + str(j) + '.png'
    sheet.save(sheet_name)
