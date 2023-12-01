
Class Report
============

:ref:`See Example 1 <Sample 01>`

This class manages the printable area on the pages, and it prints the pages into the PDF document during the
output operation. It contains a SerialFrame for the body of the report as well as one for the
header and for the footer. To build up a report you can add frames with content to the body. The body is the outermost
frame in your report.

To create a PDF document, you have to call the output function after you have added all content to the report structure.
The library will then loop recursively over the structure to calculate sizes and positions. If you need the total
number of pages in the report (e.g., in the footer or header) the PDFReport will use two passes to first count the
number of total pages. If you need that, then you have to force it by setting the count_pages attribute to True.

This is the first class that you have to instantiate if you want to create a report structure. The constructor has
a parameter which defines the page format that the library will use for the report (class PageFormat). If you do not
provide this parameter a default PageFormat will be used. You can also define a default font family that shall be
used in the report (see the section about TextStyles). The default is a Helvetica font with a size of 9 points.

..  code-block:: python

   from PDFReport import *

   # Create report instance
   #  default format A4, portrait with margins left = 20mm, top = right = bottom = 10mm
   #  Helvetica font, 9 points, black on white
   report = Report()

Now the report structure is prepared, and you can append content to it to create the report. Therefore, you can get a
reference to the report body frame which is a vertical organized SerialFrame. I describe SerialFrames later in this
document.

If you want to add content to the report body, you just create a content frame and pass the body as the first parameter.
That may look like in the following code excerpt:

..  code-block:: python

   from PDFReport import *

   # Create report instance
   report = Report()

   # Create a text frame into the body of the report
   TextFrame(report.body, "Text to print")

This example just adds some text with the NORMAL text style in a TextFrame to the report body.

Create output
-------------

:ref:`See Example 3 <Sample 03>`

The goal of the library is to create pdf documents out of the report structure. Therefore you can create a pdf file
with the *output* function in the report class. Just provide a fully qualified filename to the *output* function
to create a pdf file. The extension *.pdf* will be added in the function.

If the second parameter has the value *True* the function tries to open the created pdf file to display it.
This works only if you have installed a pdf viewer program.

..  code-block:: python

   from PDFReport import *

   # Create report instance
   report = Report()

   # Create a text frame into the body of the report
   TextFrame(report.body, "Text to print")

   # Create the pdf file
   filename = "output"
   report.output(filename, True)

It is also possible to save the report structure itself. The *save* function can be used to do that.
Just provide a fully qualified filename to the *save* function to create a json file.
The extension *.json* will be added in the function.

..  code-block:: python

   from PDFReport import *

   # Create report instance
   report = Report()

   # Create a text frame into the body of the report
   TextFrame(report.body, "Text to print")

   # Create a json file with the report structure
   filename = "output"
   report.save(filename)

If the second parameter has the value *True* the function tries to open the created json file to display it.
This works only if you have installed a textfile viewer program.

:ref:`See Example 32 <Sample 32>`

This json file can be used to create a report with data that will be provided by the class *ReportData*.

:ref:`See Example 33 <Sample 33>`


Class PageFormat
----------------

:ref:`See Example 2 <Sample 02>`

This is a structure that holds the information for a page or a set of pages in the report. It defines a page size
like A4 or Letter and the orientation of the paper (portrait or landscape). Furthermore, it limits the printable area
by the page margins. It also contains a flag which defines if the left and right margin are mirrored on even and odd
page numbers.

The following code shows how to create a *PageFormat* for a Letter sized paper in landscape mode. The left margin
is one inch, and the others are half an inch. The last parameter determines that the library will mirror the left
and right margins. You can use this instance to pass it to the constructor of a new report or in a *BreakFrame* object.

..  code-block:: python

   from PDFReport import *

   # Format letter, landscape with margins top = 1 inch and half an inch elsewhere
   page_format = PageFormat(PageSize.SIZE_LETTER, PageOrientation.LANDSCAPE,
                        25.4/2.0, 25.4, 25.4/2.0, 25.4/2.0, True);

   // Create report instance with the page_format
   report = Report(page_format)

You can find the possible page sizes in the enum *PageSize*. The enum for the orientation is *PageOrientation*.
The margins parameters are in millimeters.

Body, Header, and Footer
------------------------

:ref:`See Example 29 <Sample 29>`

The *Report* object holds the whole structure of the report. You can add content to the body by getting the reference
from the *Report* object with the attribute *body*. The body is a vertically organized *SerialFrame*. When
you add content to the body the library will print these frames one below the other.

Besides the body there is also a *SerialFrame* for a header and one for a footer which you can access via *header* and
*footer* attributes in the *Report* object. If you add content to the header and/or the footer their heights will reduce
the printable area on the page.

You can add any frame type to the header and footer but normally you will use a *PageFrame* as the main
container. With this frame type you can define on which pages the library should print the header and footer content.

In the following example I add a simple vertical container to the footer and add a box with some text. The text
is centered on the bottom of the page.

..  code-block:: python

   from PDFReport import *

   report = Report()

   vc = SerialFrame(report.footer, Direction.VERTICAL, margin_top = 5.0)
   box = BoxFrame(vc, use_full_width = True)
   TextFrame(box, "Adiuvaris - At the lake 901", TextStyle.BOLD, TextAlign.CENTER)

