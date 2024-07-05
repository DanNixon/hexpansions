# Maker Space Hexpansion App

A simple app that can be written to the Maker Space hexpansion EEPROM, which the badge will automatically load and run.

Runs a simple chasing effect as a proof-of concept.

The app runs entirely in the background and has no UI.

## Installation

General installation instructions can be found in the [badge documentation](https://tildagon.badge.emfcamp.org/hexpansions/eeprom/).

Follow the steps outlined in the documentation, using the EEPROM header information:

``` python
    header_zd24c64 = HexpansionHeader(
        manifest_version="2024",
        fs_offset=32,
        eeprom_page_size=32,
        eeprom_total_size=1024 * (64 // 8),
        vid=0xCAFE,
        pid=0x0191,
        unique_id=0x0,
        friendly_name="MS-NCL",
    )
 ```
and ensuring that `header = header_zd24c64`.

When copying the app to the hexpansion (step 6 in the docs), ensure both `app.py` and `aw9523.py` are copied to the EEPROM.

Once this is done, reboot the badge and insert the hexpansion. Some LEDs will come on at full brightness until the app is loaded, but then you should see the chasing effect.

