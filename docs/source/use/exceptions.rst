
Exceptions
==========

:ref:`See Example 28 <Sample 28>`

If the library is not able to calculate and position all the frames it will throw an exception.
This happens also if you create a circular dependency in your report tree structure. Another problem
is if you add an *ImageFrame* with invalid image file (no access or not an image). Therefore, you should catch
exceptions when you call the output function like in the following example.

..  code-block:: python

   from PDFReport import *

    report = Report()
    body = report.body

    # Endless loop
    box1 = BoxFrame(body)
    box1.add_frame(body)
    try:
        filename = "/output_28"
        report.output(filename, True)
    except OverflowError as error:
        print(error)

