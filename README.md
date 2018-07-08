# Python-QR-Code-Labels
Create custom QR Code labels with Python

Fairly simple code to produce sheets of custom QR Code labels, sequentially numbered, and formatted for printing on Avery 8161 labels.

Requires the packages pyqrcode, pypng, and PIL, and has been tested in Python 2.7.3 in Windows and Linux, 3.2.3 in Linux, and 3.4.3 in Windows 64-bit.

https://github.com/mnooner256/pyqrcode<br />
https://github.com/drj11/pypng

The following 3 lines in qr_code_label.py provide the starting number for the labels, the number of sheets to print, and the text printed on the label along with the sequential number. Only the number is encoded in the QR Code.

```python
start = 1000001
num_sheets = 4
label_text = "Field Sample"
```

These are the only 3 lines that should need any editing.

The sheets are produced as png images. They are formatted to be printed centered on a letter size (8.5" x 11") page. I've printed from both Photoshop and OpenOffice Writer.

helvetica-10.pil and helvetica-10.png are required font related files, and sheet1.png is a sample sheet of labels.

Offered without guarantee or warranty in case someone will find it useful.
