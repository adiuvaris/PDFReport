
Class ImageFrame
================

:ref:`See Example 10 <Sample 10>`

This class is derived from *ReportFrame*, and you can use it to add an image to the report. The image may be a
PNG or a JPEG file (or anything supported by the FPDF library). The image file must be readable by the *PDFReport*.

..  code-block:: python

   from PDFReport import *

   ifr = ImageFrame(body, "image.jpg", 100.0, 100.0, True)

The parameters in the constructor are all the additional attributes for an *ImageFrame*. Besides the filename of
the image, you can define the maximal width and height in millimeters and if the library will respect the aspect
ratio when it prints the image.

If you do not pass a maximal width and height, the image will use the whole width and height of the parent frame.
By default, the image keeps the aspect ratio. You can pass a maximal width or a maximal height or both. If you omit
one of them, the image uses the corresponding size of the parent.

If the aspect ratio flag is False, the image will fill the calculated rectangle. If the aspect ratio flag is True,
the image will use a rectangle as big as possible. Therefore, the frame can have white space around the picture
depending on the alignments and the given sizes.
