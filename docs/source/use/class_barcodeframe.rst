
Class BarcodeFrame
==================

:ref:`See Example 11 <Sample 11>`

This class is derived from *ReportFrame*, and you can use it to add a barcode to the report.
The barcode may be one of the enum values in BarcodeType (e.g. QRCODE, ISBN).

..  code-block:: python

   from PDFReport import *

   bcfr = BarcodeFrame(body, "text in the qr code", BarcodeType.QRCODE, 50.0, 50.0)

The parameters in the constructor are the additional attributes for the *BarcodeFrame*.
First there is the text of the barcode. Then follows the type of barcode. At last, you can pass a maximal
width and height in millimeters for the barcode image.

If you do not pass a maximal width and height, the barcode image will use the whole width and height of the
parent frame. You can pass a maximal width or a maximal height or both. If you omit one of them, the barcode
frame uses the corresponding size of the parent.

The barcode type defines the form of the barcode image. The code image uses as much space as possible in the
calculated rectangle. Therefore, the frame can have white space around the code image depending on the
alignments and the given sizes.
