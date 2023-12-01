
FPDF
====

As mentioned earlier the PDFReport library uses the FPDF library to create PDF documents.
All code which accesses the FPDF library is encapsulated in the class Renderer.

Fonts
-----

This library can use the font families that are available for FPDF. There are three core font
families Helvetica, Courier, and Times that you can use in the PDFReport.

It is possible to add more fonts to the FPDF library. See the documentation of FPDF if you need that.

Page sizes
----------

You can use all defined page sizes in the enum PageSize for reports that you generate with the
PDFReport (e.g., PageSize.SIZE_A4 et cetera). The list of the possible page formats can be found in the enum.

Colors
------
Colors in this library are strings containing the RGB hex values as in HTML colors. To make it
more visible that a string is a color you should add an ‘#’ at the first position of the string but it is
not necessary. The hex characters in the string can be uppercase or lower case.

..  code-block:: python

   red = '#FF0000'

PDFReport uses the Pillow library to access image data. Therefore you can use the colors which are defined
in Pillow by their names. The following codes shows how to do that.

..  code-block:: python

   from PIL import ImageColor

   color = ImageColor.colormap["lime"]




Text Alignments
---------------

Text alignment which are supported by FPDF. There is an enum in PDFReport: TextAlign

   •	LEFT
   •	RIGHT
   •	CENTER
   •	JUSTIFY


Frame Alignments
----------------

There is an enum for horizontal and vertical alignments of frames.
Horizontal alignment (HAlign)

   •	LEFT
   •	RIGHT
   •	CENTER

Vertical alignment (VAlign)

   •	TOP
   •	MIDDLE
   •	BOTTOM

So, whenever a function needs a parameter of HAlign or VAlign use one of these values.
