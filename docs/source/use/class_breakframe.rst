
Class BreakFrame
================

:ref:`See Example 9 <Sample 09>`

The *BreakFrame* is derived from *ReportFrame*, but it holds no content, and it does not use the attributes of the
*ReportFrame* class. You can use it to manually force a page break.

..  code-block:: python

   from PDFReport import *

   bf = BreakFrame(body)

This class offers one additional attribute of type *PageFormat*. With that you can change the page format
that the library will use for the pages after the page break. The new page format keeps valid until you insert
another manual page break with a new page format.

..  code-block:: python

   from PDFReport import *

   # Add a manual page break and change the settings to
   #     A5 portrait and set the margins - mirror the left and right margins
   pageFormat = PageFormat('A5', 'P', 20.0, 10.0, 10.0, 10.0, True)
   bf = BreakFrame(body, pageFormat)
