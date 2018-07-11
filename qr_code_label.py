#! /python

from pyqrcode import QRCode
from PIL import Image, ImageDraw, ImageFont

'''
Generates sheets of 10 labels with sequentially numbered
QR codes formatted for printing on Avery 8161 labels.

George S. Williams  physicist@websterling.com  07/2018
'''

start = 1
num_sheets = 4
label_text = "This Is Sample Label Text"

count = start - 1
font = ImageFont.load('courR08.pil')

for j in range(1, num_sheets + 1):
    sheet = Image.new('RGBA', (590, 720), (255, 255, 255, 255))

    for i in range(0, 20):
        count = count + 1
        seq = str(count).zfill(7)
        qr = QRCode(seq)
        qr.png('qr.png', scale=2)

        qr_img = Image.open('qr.png', 'r')
        qr_img_w, qr_img_h = qr_img.size
        label = Image.new('RGBA', (288, 72), (255, 255, 255, 255))
        bg_w, bg_h = label.size
        offset = ((bg_h - qr_img_h) // 2, (bg_h - qr_img_h) // 2)
        label.paste(qr_img, offset)

        d = ImageDraw.Draw(label)
        label_h_offset = int(155 - (5 * len(label_text) / 2))
        d.text((label_h_offset, 22), label_text, font=font, fill=(0, 0, 0))
        seq_h_offset = int(155 -(5 * len(seq) / 2))
        d.text((seq_h_offset, 37), seq, font=font, fill=(0, 0, 0))

        h_offset = int(i % 2 * 302)
        row = int(abs(i / 2))
        y_offset = int(row * 72)
        sheet.paste(label, (h_offset, y_offset))

    sheet_name = 'sheet' + str(j) + '.png'
    sheet.save(sheet_name)
