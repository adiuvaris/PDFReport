
Class LineFrame
===============

:ref:`See Example 8 <Sample 08>`

This is another simple frame type. It can be used to add various kinds of lines to a report. You can add
horizontal or vertical lines to the report by adding such an object to a container frame.

..  code-block:: python

   from PDFReport import *

   lf = LineFrame(body, Direction.HORIZONTAL, 0.5, "#00FF00", 120.0)

These are the parameters to the constructor.

   •	direction - horizontal or vertical (Direction.HORIZONTAL, Direction.VERTICAL)
   •	extent - Extent of the line in millimeters
   •	color
   •	length - length in millimeters

A *Pen* object (see next section) prints the line. Therefore, you can change the look of the line by changing
the line attributes. You can use solid or dotted or dashed lines by setting a pen to the frame.

..  code-block:: python

   from PDFReport import *

   # Print a centered dotted line, extent 0.2mm and of blue color
   lf = LineFrame(body, Direction.HORIZONTAL)
   lf.pen = Pen(0.2, "#0000FF", 'dot')
   lf.length = 50.0
   lf.h_align = HAlign.CENTER


Class Pen
---------

*Pen* objects describes line styles. The *LineFrame* (as seen in the previous section) but also the *BoxFrame* use pens.
A pen contains a color, an extent (thickness of the line) and a line style (e.g., solid, dashed et cetera).
You can create a new pen as follows.

..  code-block:: python

   pen = Pen(0.2, "#0000FF", LineStyle.DOT)

You can pass all the attributes or none of them. In this case you will get a default pen which has an extent
of 0.1mm and it is a solid black line. *PDFReport* accepts the following values for the line style
parameter (enum *LineStyle*):

   •	SOLID
   •	DASH
   •	DOT

