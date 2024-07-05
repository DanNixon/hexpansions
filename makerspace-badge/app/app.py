import app
from .aw9523 import *

# Index of the list is the LED number according to the pinmap (except zero indexed) https://github.com/DanNixon/hexpansions/blob/main/makerspace-badge/README.md
# First value is the LED driver number (0 or 1)
# Second value is the LED driver address for that LED
# This could probably be much nicer
_MS_PINMAP = [ 
    (0, 0x2B),
    (0, 0x2C),
    (0, 0x2D),
    (0, 0x2E),
    (0, 0x2F),
    (0, 0x2A),
    (0, 0x29),
    (0, 0x28),
    (0, 0x27),
    (0, 0x26),
    (0, 0x25),
    (0, 0x24),
    (0, 0x23),
    (0, 0x22),
    (0, 0x21),
    (0, 0x20),
    (1, 0x2B),
    (1, 0x2C),
    (1, 0x2A),
    (1, 0x29),
    (1, 0x28),
    (1, 0x27),
    (1, 0x26),
    (1, 0x25),
    (1, 0x24),
    (1, 0x20),
    (1, 0x21),
    (1, 0x22),
    (1, 0x23)
]

class MSHexpansionApp(app.App):
    def __init__(self, config=None):
        self.app = app
        self.AW9523 = None # This will actually be a list of two AW9523 objects since there's 2 on the hexpansion
        self.hexpansion_config = config
        if self.hexpansion_config:
            self.reinit_hexpansion()
        self.idx = 0 # Used for the animation

    def all_leds_off(self):
        if self.AW9523:
            for pin in _MS_PINMAP:
                self.AW9523[pin[0]][pin[1]] = 0

    def reinit_hexpansion(self):
        if self.hexpansion_config:
            self.AW9523 = [AW9523(self.hexpansion_config.i2c,address=0x5A), AW9523(self.hexpansion_config.i2c, address=0x5B)]
            self.all_leds_off()

    def update(self, delta):
        # Nothing here because everything happens in the background.
        return None

    def background_update(self, delta):
        if self.AW9523:
            try:
                self.all_leds_off()
                expander_number, address = self.get_led(self.idx)
                self.AW9523[expander_number][address] = 50 # Can be up to 255, but That's Too Bright
                self.idx += 1
                if self.idx > 28:
                    self.idx = 0
            except AttributeError:
                print("Hexpansion removed!")
        else:
            self.reinit_hexpansion()

    def draw(self, ctx):
        # Nothing to draw
        return None

    def get_led(self, index):
        exp =  _MS_PINMAP[index][0]
        addr = _MS_PINMAP[index][1]
        return exp,addr

__app_export__ = MSHexpansionApp