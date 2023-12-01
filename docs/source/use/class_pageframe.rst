
Class PageFrame
===============

:ref:`See Example 24 <Sample 24>`

This is also a *ContainerFrame*. With this frame type you can control on which pages the library prints the
content of this frame. You can define that the content prints on a certain page or on odd or even pages or on all
pages without the first page. You can use this kind of frame type in headers and footers if you want different headers
and/or footers on even and odd pages, but it is possible to use it anywhere.

The following code creates a *PageFrame* that is printed on all pages but not on the first page. The content is
a box with a grey background using the full width of the printable area and a height of 15mm.

..  code-block:: python

   from PDFReport import *

   pf = PageFrame(header, PageFrame.ON_ALL_BUT_FIRST_PAGE);
   box = Box(pf)
   box.setUse_full_width(True)
   box.setHeight(15.0)
   box.setBackground("#EEEEEE")

The second parameter of the constructor is the page number on which the content has to be print or one of the
following values. You find them in the class *PageFrame*. Any positive number for the *on_page_nr* parameter will
print the frame on exactly this page and only there.

..  code-block:: python

    ON_ALL_PAGES = 0
    ON_ODD_PAGES = -1
    ON_EVEN_PAGES = -2
    ON_ALL_BUT_FIRST_PAGE = -3

