
Units of measurement
====================

All sizes, extents and positions in the library functions are expected in millimeters as float values.
Some frame types allow it to define the width in percent of the surrounding frame.

In these cases, the widths are expected as strings e.g., “35.0%”. The percent sign is not necessary
but makes your code more readable, and it is clearer what you mean. The parameters for these functions
are defined as Any and if a string arrives it will be managed as percent value.

