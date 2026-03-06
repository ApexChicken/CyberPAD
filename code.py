import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

# -----------------------------------------------
# PIN ASSIGNMENTS
# 4 buttons wired as a 2x2 matrix
# Adjust these if your PCB routes to different pins
# -----------------------------------------------
keyboard.col_pins = (board.D0, board.D1)   # 2 columns
keyboard.row_pins = (board.D2, board.D3)   # 2 rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# -----------------------------------------------
# KEYMAP
# Layout (top-down view of macropad):
#   [ KEY1 ] [ KEY2 ]
#   [ KEY3 ] [ KEY4 ]
#
# Customize these keycodes to whatever you want.
# Examples of useful keycodes:
#   KC.MUTE        — mute audio
#   KC.VOLU        — volume up
#   KC.VOLD        — volume down
#   KC.MPLY        — play/pause
#   KC.LCTL(KC.C)  — Ctrl+C (copy)
#   KC.LCTL(KC.V)  — Ctrl+V (paste)
#   KC.LCTL(KC.Z)  — Ctrl+Z (undo)
#   KC.F5          — refresh
# -----------------------------------------------
keyboard.keymap = [
    [
        KC.MUTE,           KC.VOLU,   # top row
        KC.MPLY,           KC.VOLD,   # bottom row
    ]
]

if __name__ == '__main__':
    keyboard.go()
