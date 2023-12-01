
Text styles
===========

The PDFReport library uses text styles to define the font and the appearance of text in a report.
There is a list of predefined text styles which you can use in a report. A text style consists of a font
family (e.g., Helvetica, Courier et cetera), some font styles (bold, italic, underline) and a size in points.
A text style also defines the text color and the background color.

The text styles are globally managed, so you can access them by their names or by reference. For that you
can use the class TextStyles which holds a dictionary with all the defined text styles.

The default basic text style (NORMAL) uses the font family Helvetica and has a size of nine points.
The text color is black, and the background is white. You can change the font-family, the font size and the
text color of that NORMAL text style during the instantiation of the main report object.

The predefined text styles are based on a text style named NORMAL. So all derived text styles will use
the same font family and colors. The other attributes as the size and the font style (bold, italic and underline)
may be changed.

The following list shows the differences of the styles in relation to the NORMAL style.

   •	NORMAL: Helvetica, 9 points, black on white
   •	SMALL: one point smaller
   •	HEADING1: nine points taller and bold
   •	HEADING2: six points taller and bold
   •	HEADING3: three points taller and bold and italic
   •	HEADING4: one point taller and bold and italic
   •	BOLD: bold
   •	ITALIC: italic
   •	UNDERLINE: underlined
   •	FOOTER: one point smaller
   •	HEADER: like FOOTER
   •	TABLE_HEADER: one point smaller and bold
   •	TABLE_ROW: one point smaller
   •	TABLE_SUBTOTAL: one point smaller and italic
   •	TABLE_TOTAL: one point smaller and bold

You can define new text styles which are based on any other text style. To access these text styles, you will
use their name. I will describe the usage of text style attributes in detail later in this documentation.
