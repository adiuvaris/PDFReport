
Class SerialFrame
=================

:ref:`See Example 26 <Sample 26>`

This is a derivation of the *ContainerFrame* class which can contain a series of frames. A *SerialFrame* has a
direction which is either *horizontal* or *vertical*. All frames may contain any kind of content or other
container frames.

The following example shows how you instantiate a horizontal *SerialFrame*. For a vertical *SerialFrame* you
obviously use the parameter *Direction.VERTICAL*.

..  code-block:: python

   from PDFReport import *

   sf = SerialFrame(body, Direction.HORIZONTAL)

There is only one additional attribute for this class which defines how the library places the frames on the page.
Either it can be horizontally i.e., one frame right to the previous one or vertically which means the frames are
one below the other.

As mentioned in the last section you will use the *BoxFrame* and the *SerialFrame* very often to create a report.
Because you can add containers into containers you can create complex tree structures.
