Class TextStyles
================

This is merely a container for all the defined text styles. They are managed in a dictionary with the name of the
text style as key and the definition of the *TextStyle* as value.

You can get a reference to a text style by the name of the text style as shown in the following example.

..  code-block:: python

   ts = TextStyles[TextStyle.TABLE_HEADER]

You can change any attribute of the text style. Any further use of that text style will then use the newly defined
attributes.

The following code changes the text color for text of table headers to red. Any table which is added to the
report structure afterwards will use this style.

..  code-block:: python

   ts = TextStyles[TextStyle.TABLE_HEADER]
   ts.text_color = "#FF0000"


If you define new text styles they will be added to the global dictionary of *TextStyles* as well. So you
can access them with the given name.

..  code-block:: python

   ts = TextStyle("my_text_style", size=24.0, text_color="#0000FF")

   ts = TextStyles["my_text_style"]

Whenever you need a text style for the report you can use the name or a reference to a text style.
In the report object the text style will be copied so that any change to a global text style in the class
TextStyles will have no effect to the previously defined part of the report.

If you want to change any attribute of a defined text output object as e.g. a TextFrame, you have to
access the text_style attribute of the TextFrame class and change the text style attribut there.

..  code-block:: python

   ts = TextStyle("my_text_style", size=24.0, text_color="#0000FF")
   tf1 = TextFrame(report.body, "Blue text", "my_text_style")
   tf2 = TextFrame(report.body, "Red text", "my_text_style")
   tf2.text_style.text_color = "#FF0000"

Both text frames in the example are defined using the text style "my_text_style". Internally they will create
a new instance of the class TextStyle with the same attributes as "my_text_style". But the text style in
the second text frame is changed to print the text in another color.


Predefined text styles
----------------------

As mentioned earlier there is a list of predefined text style. They will be created during the creation of
the class *Report*. The constructor of the class *Report* has parameters to change the default font style
with the name *NORMAL*. You can change the default font family, the base size and the text color.
All other predefined text styles will inherit these settings and are modified relative to the text style *NORMAL*.

The following list shows the differences of the styles in relation to the *NORMAL* style.

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

You can use these text styles with their names to create content with text.

..  code-block:: python

   TextFrame(report.body, "This is a title", TextStyle.HEADING1)

The text styles with *TABLE_* in the name will be implicitly used in tables (*TableFrame*). You can change
them at any point during the creation of a *TableFrame* or *TableCells*.
