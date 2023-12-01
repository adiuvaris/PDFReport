
Class ReportFrame
=================

*ReportFrame* is an abstract base class which defines some functions and attributes which are inherited by concrete
classes like *TextFrame*. I will describe these concrete classes in later sections of this document.

As said earlier in this document, a frame is a rectangular region on the paper that may have some content like
text or an image or other things.

The class offers the following attributes. They have getters and setters.

   •	h_align, v_align - horizontal and vertical alignment
   •	margin_left, margin_top, margin_right, margin_bottom - margins on all four sides
   •	use_full_height, use_full_width - flags if the frame uses the whole possible space
   •	keep_together - flag if the frame and all its content kept together on the same page
   •	max_width, max_height - maximal dimensions of the frame

These attributes are available in all the derived classes. They control the calculation of sizes and positions of frames.

*ReportFrame* offers a lot of functions that will be used by the Report class to calculate the size and position of the frame.
Normally you must not use any of these functions.

Class ContainerFrame
--------------------

This class is a derivation of the class *ReportFrame* an inherits all the attributes from it. There is only one additional
attribute which can hold an array of frames. It is an abstract base class for the *SerialFrame* or *BoxFrame* classes which
I describe later in this document.

This class offers all the necessary functions to manage the array of frames. The array can hold any kind of frame type
which is derived from *ReportFrame*.

A new frame uses the *add_frame* function of its parent frame to add itself to the parents list of frames. The newly added
frame is added at the end of the container. There are also functions to get a certain frame (get_frame or clear_frames).
Because a container frame can contain other containers you can create a highly recursive tree structure.

The library calculates the size of the frame by calculating recursively the sizes of all the inner frames.
