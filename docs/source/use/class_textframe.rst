
Class TextFrame
===============

:ref:`See Example 3 <Sample 03>`

The *TextFrame* class is derived from *ReportFrame* and holds some kind of text. A *TextFrame* needs a text and a text
style. If no text style is given the library uses the *NORMAL* text style. It is a simple frame type with no other
frames in it. You can add a text frame to any container frame using it as the first parameter in the constructor.

..  code-block:: python

   from PDFReport import *

   report = Report()
   TextFrame(report.body, "Text to print")

The *PDFReport* tries to print the text into the given frame. If necessary, it inserts line breaks or even page
breaks to fit the text into the report. The surrounding frame defines the width of the text. In the example the
width is the printable area of the paper because the text is added to the main *body* frame of the report.

The text style controls the output of the text. You can use any of the predefined text styles or you can
create your own text styles. If there is no *text_style* parameter to the *TextFrame* constructor the text
style *NORMAL* will be used.

The following example uses the predefined text style *BOLD* to print the text.

..  code-block:: python

   from PDFReport import *

   report = Report()
   TextFrame(report.body, "Text to print", TextStyle.BOLD)

By default, the library splits the text that does not fit into the given width of a frame into multiple lines,
but you can define that the text should be cut off after one line. For that you have to set the *word_wrap*
attribute to *False*.

The text may contain some variables which will be replaced during the output operation. You have to surround
the variable names by square brackets. You can use:

   •	VAR_PAGE - the page number
   •	VAR_TOTAL_PAGES - the total number of pages in the document.

You can use these variables at any place, but they are often used in headers or footers.

 ..  code-block:: python

   from PDFReport import *

   tf = TextFrame(report.header, "Page [VAR_PAGE] of [VAR_TOTAL_PAGES]")

The renderer replaces the texts during the rendering, and it will keep the alignments correct.
If you use the total number of pages, you have to inform the library to calculate the pages by setting
*count_pages* to *True* of your *Report* object.
