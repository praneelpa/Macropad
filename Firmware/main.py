from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import send_string
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# GP0 = Sleep
# GP1 = Screenshot
# GP2 = Clipboard
# GP3 = Undo/Redo
# GP4 = App Switch
# GP7 = Quit

keyboard_pins = {
    "GP1": KC.TSFT4,
    "GP1_hold": KC.TSFT3,
    "GP2": KC.LGUI(KC.C),
    "GP4": KC.LGUI(KC.TAB),
    "GP3": KC.LGUI(KC.Z),
    "GP3_hold": KC.LGUI(KC.LSFT(KC.Z)),
    "GP0": KC.LGUI(KC.F9),
    "GP7": KC.LGUI(KC.Q),
}

keyboard_layer = [
    [
        KC.TSFT4, KC.LGUI(KC.C), KC.LGUI(KC.TAB),
        KC.LGUI(KC.Z), KC.LGUI(KC.F9), KC.LGUI(KC.Q)
    ]
]

if __name__ == "__main__":
    keyboard.go()