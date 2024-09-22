"""
@autor: MBI
Description: Script to use of Qt namespace. Using bitwase operators OR and And (|) (&),to get the set 
flags in de input value.

Identifier        Value (hex) Value (decimal)             Description
Qt.AlignLeft      0x0001       1                          Aligns with the left edge.
Qt.AlignRight     0x0002       2                          Aligns with the right edge.
Qt.AlignHCenter   0x0004       4                          Centers horizontally in the available space.
Qt.AlignJustify   0x0008       8                          Justifies the text in the available space.
Qt.AlignTop       0x0020       32                         Aligns with the top.
Qt.AlignBottom    0x0040       64                         Aligns with the bottom.
Qt.AlignVCenter   0x0080       128                        Centers vertically in the available space.
Qt.AlignBaseline  0x0100       256                        Aligns with the baseline.
"""
#==== Packages ====#
from PyQt5.QtCore import Qt 
#==== Examples ====#
# Use bitwise OR (|)

print(int(Qt.AlignLeft | Qt.AlignTop))

print(int(Qt.AlignLeft | Qt.AlignLeft | Qt.AlignTop))

print(int(Qt.AlignLeft | Qt.AlignLeft | Qt.AlignLeft))

# Checing compound flags
aling = Qt.AlignLeft
print(aling == Qt.AlignLeft)

align = Qt.AlignLeft | Qt.AlignTop
print(align == Qt.AlignLeft | Qt.AlignTop )

alignmet = Qt.AlignLeft | Qt.AlignTop
print(alignmet == Qt.AlignLeft)

# Use bitwise And (&)
print(alignmet & Qt.AlignLeft)
print(alignmet & Qt.AlignRight)



