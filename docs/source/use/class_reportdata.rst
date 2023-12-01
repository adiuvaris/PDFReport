Class ReportData
================

The class *ReportData* looks like the following code excerpt. As you can see it is possible to provide dynamic
data for texts, images, barcodes and tables. This class is abstract and you cannot use it directly.
You have to create your own derivation of that class.

.. code-block:: python

   from abc import ABCMeta

   class ReportData(metaclass=ABCMeta):

      def on_text_data(self, text_frame):
         pass

      def on_barcode_data(self, barcode_frame):
         pass

      def on_image_data(self, image_frame):
         pass

      def on_table_data(self, table_frame):
         pass

The following sections show the possibilities of the *ReportData* class.

Naming frames
-------------

If you want to use a report with dynamic data provided by a derivation of *ReportData* you have to name the
frames so that you can identify them when you create the real report with data.

Every frame class has an optional parameter *frame_id* that you can use the name the frames. Only the frames
that you will use to fill with dynamic data need its own unique names. If you don't provide a *frame_id* the
library names the ids automatically (you can see that in the json-output of a report).

The following sample shows how to create a text frame with the name *TEXT_1*.

.. code-block:: python

   from PDFReport import *

   # Create report instance
   report = Report()

   # Create a text frame into the body of the report
   TextFrame(report.body, frame_id="TEXT_1")


Save the report structure
-------------------------

:ref:`See Example 32 <Sample 32>`

It is possible to save a report structure to a json file. The saved file can be loaded into an instance of
the report class and you can use it to create a report with data from a dataprovider.

Just call the *save* function of the report class to create a json file out of a previously created report structure.

.. code-block:: python

   from PDFReport import *

   # Create report instance
   report = Report()

   # Create report structure (frames)
   ...

   filename = "output_32"
   report.save(filename)


Create a report from a saved json file
--------------------------------------

:ref:`See Example 33 <Sample 33>`

Out of a saved json file you can create reports with data that will be provided by an instance of a class
that you have derived from *ReportData*.

To use a saved report structure you have to define a class derived from *ReportData* as the following sample shows.
The callback function will be called during the output function of the report.

.. code-block:: python

   class DataProvider(ReportData):

      def on_text_data(self, text_frame: TextFrame):
         if text_frame.frame_id == "TEXT_1":
            text_frame.text = "This ist the text for the frame named: Text 1"

You need to identify the frame and can than set the data for that frame. In the example code the text frame with the id
*TEXT_1* will be filled with some text.

Of course it is not necessary to use static data in the data provider. You can create more classes or functions
to provide data from the program, some files or even a database.

The following code shows how the saved report is loaded into the report instance. Than an instance of the
dataprovider will be created. It will be used to pass it to the output function so the report can callback
to ask for data that should be use for named frames.

.. code-block:: python

   class DataProvider(ReportData):

      def on_text_data(self, text_frame: TextFrame):
         if text_frame.frame_id == "TEXT_1":
            text_frame.text = "This ist the text for the frame named: Text 1"

   def sample():
       report = Report()

       filename = "output"
       report.load(filename)

       data = DataProvider()
       report.output(filename, True, data)



