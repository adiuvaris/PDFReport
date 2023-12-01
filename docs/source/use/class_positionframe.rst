
Class PositionFrame
===================

:ref:`See Example 23 <Sample 23>`

The library places the content of this container on an absolute position on the page. When you create such an object,
you have to define an offset in millimeters from the left and the top border of the *paper*. These coordinates define
the top left corner of the frame. You can add a third parameter in the constructor. This parameter defines if the
library is allowed to overlay other frames with this one. The default for the overlay flag is False.

The following code creates a *PositionFrame* and adds a *BoxFrame* to it. The library places the top left corner of
the box at the coordinates 60mm from the left side and 130mm from the top of the paper. It will not print over
other frames and would create a page break if other content is in the way.

..  code-block:: python

   from PDFReport import *

   fix = PositionFrame(body, 60.0, 130.0)
   box = BoxFrame(fix)
   box.setWidth(100.0)
   box.setHeight(50.0)
   box.setBorderPen(new Pen(0.1, "#CCCCCC"))

The library prints the content of this container at the defined position (top left corner). But it will
normally not overwrite any existing content. If the space that is needed for the content of a *PositionFrame*
overlaps with any other content on the page, the library will add a page break.

If you want to print a content on any case at a certain spot you can add the third parameter with the value True.
This is also necessary if you want to define offsets that are outside of the printable area.
