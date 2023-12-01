========
Overview
========

PDFReport is a Python library to generate dynamic PDF reports using the FPDF library to create a PDF document.

The library works with nested rectangular regions (frames) on the paper where you can define the sizes in
millimeters or in percent of the surrounding rectangle or the library can calculate them based on the content.
Each rectangle can have a different kind of content (e.g., some text, an image, a barcode).

Frames are arranged in a hierarchy. When creating each child frame, its parent frame is passed as the
first argument to the constructor.


.. toctree::
   :maxdepth: 2
   :caption: Classes:

   a_first_example
   basic_concepts
   units_of_measurement
   textstyles
   example_programs


