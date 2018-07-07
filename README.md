# Python-QR-Code-Labels
Create custom QR Code labels with Python

Fairly simple code to produce sheets of custom QR Code labels, sequentially numbered, and formatted for printing on Avery 8161 labels.

Requires the packages pyqrcode, and PIL compiled with ImageFont support.

The following 2 lines provide the starting number for the labels and the number of sheets to print. These are the only 2 lines that should neeed any editing.

start = 1000001
num_sheets = 4

The sheets are produced as png images. 
