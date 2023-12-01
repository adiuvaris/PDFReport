Sample 22
=========

The ‘body’ that has been used in all examples is in fact a vertical SerialFrame.
Each frame added to the body will be printed just below the preceding one (in the flow of the document).

First there is a horizontal SerialFrame added to the body with a left aligned text in a box with a width of 50mm.
Right to the first frame follows a bold text in box of width 120m. The texts are close because there is no padding.

Then a second horizontal SerialFrame is added to the body and will be printed therefore below the first one.
Three columns of justified text in separate boxes, each with a width of 55mm. The columns have a distance of 4mm.

A SerialFrame can also hold other frame types which is shown in the next section. On the left side there is a
barcode followed by a distance of 5mm. Then follows an image and on the right side there is a 50mm width box with text.

BoxFrames and SerialFrames can also be used to create aligned labels and texts. The labels have a fixed width of
25mm and are right aligned. The texts will use the rest of the width of the surrounding frame and are left aligned

.. autofunction:: sample_22.sample_22


Output Sample 22
----------------

:download:`Click here to see the output of sample 22 <output/output_22.pdf>`
