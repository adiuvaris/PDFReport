Sample 28
=========

There are situations where the library can’t create a report. In these cases an exception is thrown.

One problem is an endless loop because of a circle dependency in the report structure.

A problem is also if a frame should be kept together but the size of the complete frame is bigger than the space on a page.

Another problem is when there is no space left in frame to put another frame into it.
In the example the first text uses the whole width so the second text does not get any space.

If a PositionFrame uses offset values which are outside the printable area and the frame may not overlay
other frames an exception is thrown.

If the file which name is passed to an ImageFrame does not exist or is not a valid image file an exception is thrown.

.. autofunction:: sample_28.sample_28


Output Sample 28
----------------

Endless recursion loop in the report structure.

Keep together frame bigger than one page!

No space left in frame for another frame!

Non overlay PositionFrame is outside the printable area

Image file does not exist: