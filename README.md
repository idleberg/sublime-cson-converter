# Converter

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/CSON%20Converter.svg?style=flat-square)](https://packagecontrol.io/packages/CSON%20Converter)
[![GitHub release](https://img.shields.io/github/release/idleberg/sublime-cson-converter.svg?style=flat-square)](https://github.com/idleberg/sublime-cson-converter/releases)
[![Travis](https://img.shields.io/travis/idleberg/sublime-cson-converter.svg?style=flat-square)](https://travis-ci.org/idleberg/sublime-cson-converter)

Converts CSON, JSON and XML

## Installation

### Package Control

1. Make sure you already have [Package Control](https://packagecontrol.io/) installed
2. Choose *“Install Package”* from the Command Palette (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>)
3. Type *Converter* and press <kbd>Enter</kbd>
4. Repeat steps 2 and 3 to install *“Better CoffeeScript”*

With [auto_upgrade](http://wbond.net/sublime_packages/package_control/settings/) enabled, Package Control will keep all installed packages up-to-date!

### Manual installation

Since [package dependencies](https://packagecontrol.io/docs/dependencies) are handled by Package Control, manual installation is not advised! If you still want to install from source, you probably know what you are doing so we won’t cover that here.

## Usage

The [Command Palette](http://docs.sublimetext.info/en/latest/reference/command_palette.html) currently offers the following commands:

* Convert: CSON to JSON
* Convert: CSON to XML
* Convert: JSON to CSON
* Convert: JSON to XML
* Convert: XML to CSON
* Convert: XML to JSON

**Note:** Since conversion is based on scope, make sure the a supported CoffeeScript package is installed as well. Using [Better CoffeeScript](https://packagecontrol.io/packages/Better%20CoffeeScript) is recommended, though [CoffeeScript](https://packagecontrol.io/packages/CoffeeScript), [IcedCoffeeScript](https://packagecontrol.io/packages/IcedCoffeeScript) and [Mongoose CoffeeScript](https://packagecontrol.io/packages/Mongoose%20CoffeeScript) are also supported.

### Keyboard Shortcuts

*The following examples all use the macOS shortcuts, for Linux or Windows use <kbd>Ctrl</kbd>+<kbd>Alt</kbd> rather than <kbd>Cmd</kbd>+<kbd>Alt</kbd>.*

Memorizing the keyboard shortcuts for conversion is easy. Just think of <kbd>C</kbd> for CSON, <kbd>J</kbd> for JSON, and <kbd>X</kbd> for XML:

Action       | Mnemonic | Shortcut
-------------|----------|-----------------------------------------------------------
CSON to JSON | “C to J” | <kbd>Ctrl</kbd>+<kbd>C</kbd>, <kbd>Ctrl</kbd>+<kbd>J</kbd>
CSON to XML  | “C to X” | <kbd>Ctrl</kbd>+<kbd>C</kbd>, <kbd>Ctrl</kbd>+<kbd>X</kbd>
JSON to CSON | “J to C” | <kbd>Ctrl</kbd>+<kbd>J</kbd>, <kbd>Ctrl</kbd>+<kbd>C</kbd>
JSON to XML  | “J to X” | <kbd>Ctrl</kbd>+<kbd>J</kbd>, <kbd>Ctrl</kbd>+<kbd>X</kbd>
XML to CSON  | “J to C” | <kbd>Ctrl</kbd>+<kbd>X</kbd>, <kbd>Ctrl</kbd>+<kbd>C</kbd>
XML to JSON  | “J to X” | <kbd>Ctrl</kbd>+<kbd>X</kbd>, <kbd>Ctrl</kbd>+<kbd>J</kbd>

### Settings

Some of the default conversion settings can be modified from the *Package Settings* menu:

* Indentation level (`int`)
* Sort keys (`boolean`)

# License

This work is licensed under the [The MIT License](LICENSE).

## Donate

You are welcome support this project using [Flattr](https://flattr.com/submit/auto?user_id=idleberg&url=https://github.com/idleberg/sublime-cson-converter) or Bitcoin `17CXJuPsmhuTzFV2k4RKYwpEHVjskJktRd`
