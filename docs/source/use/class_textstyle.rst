
Class TextStyle
===============

:ref:`See Example 5 <Sample 05>`

You can find the list of the predefined text styles earlier in this document and in the next section about
the class *TextStyles*.

You can create new text styles and give them a name to use it later at any point in the program like the predefined text
styles. You define a new text style by calling the constructor for a *TextStyle*. The constructor expects a
name for the new text style. This name must be unique, if you try to add a text style with a name that already exists
you will get an Exception. You may also pass a base text style and attributes for the new text style.
If you omit the base style parameter the predefined text style NORMAL will be used as base style.

If you pass an attribute it will overwrite the value of that attribute from the base style. If you don't pass
an attribute it will obviously use the value from the passed base style. If no base style is provided the
attribute value will be taken from the NORMAL text style.

The following example shows how to create a new text style based on the NORMAL text style. The new text style
gets the name *BigRed* and changes the attribute for the size to a value of 36 points and the text color to red.
The library uses the values from the NORMAL text style for all other attributes (e.g. the font family).

..  code-block:: python

   from PDFReport import *

   # Create a text style with the name "BigRed", 36 points tall and red
   ts = TextStyle("BigRed", size = 36.0, text_color ="#FF0000")

I describe the attributes of a text style in the next section.

You can use the text style by its name or you can pass the reference ts to a frame type that needs a text style, e.g.
*TextFrame* or *TableCell*.


TextStyle Attributes
--------------------

:ref:`See Example 6 <Sample 06>`

The text styles control the format of text output. Text styles define the font as well as the text color
and the background color. There are attributes for all of the attributes of a text style. You can define the
following attributes in a text style:

   •	bold
   •	italic
   •	underline
   •	size – absolute size of the font in points
   •	font_family – the font e.g., Helvetica
   •	text_color
   •	background_color

The default text style NORMAL has a font size of nine points and uses the font family Helvetica. The text color is black,
and the background is white. The flags bold, italic and underline are False. These settings can be changed
in the *Report* class.

