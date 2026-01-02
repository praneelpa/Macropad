from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(TapDance())

# TapDance keys
screenshot_td = KC.TD(
    KC.LGUI(KC.LSFT(KC.N4)),  # Tap → Cmd+Shift+4
    KC.LGUI(KC.LSFT(KC.N3))   # Hold → Cmd+Shift+3
)

undo_redo_td = KC.TD(
    KC.LGUI(KC.Z),            # Tap → Undo
    KC.LGUI(KC.LSFT(KC.Z))    # Hold → Redo
)

keyboard.pins = {
    "GP27": screenshot_td,     # Screenshot
    "GP2": KC.LGUI(KC.C),      # Clipboard
    "GP4": KC.LGUI(KC.TAB),    # App switch
    "GP3": undo_redo_td,       # Undo / Redo
    "GP26": KC.LGUI(KC.F9),    # Sleep
    "GP7": KC.LGUI(KC.Q),      # Quit
}

keyboard.keymap = [
    [
        screenshot_td,
        KC.LGUI(KC.C),
        KC.LGUI(KC.TAB),
        undo_redo_td,
        KC.LGUI(KC.F9),
        KC.LGUI(KC.Q),
    ]
]

if __name__ == "__main__":
    keyboard.go()