# CSON Converter

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/CSON%20Converter.svg?style=flat-square)](https://packagecontrol.io/packages/CSON%20Converter)
[![GitHub release](https://img.shields.io/github/release/idleberg/sublime-cson-converter.svg?style=flat-square)](https://github.com/idleberg/sublime-cson-converter/releases)
[![Travis](https://img.shields.io/travis/idleberg/sublime-cson-converter.svg?style=flat-square)](https://travis-ci.org/idleberg/sublime-cson-converter)

Convert JSON to CSON, and vice versa.

## Installation

### Package Control

1. Make sure you already have [Package Control](https://packagecontrol.io/) installed
2. Choose *“Install Package”* from the Command Palette (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>)
3. Type *CSON Converter* and press <kbd>Enter</kbd>
4. Repeat steps 2 and 3 to install *“Better CoffeeScript”*

With [auto_upgrade](http://wbond.net/sublime_packages/package_control/settings/) enabled, Package Control will keep all installed packages up-to-date!

### Manual installation

Since [package dependencies](https://packagecontrol.io/docs/dependencies) are handled by Package Control, manual installation is not advised! If you still want to install from source, you probably know what you are doing so we won’t cover that here.

## Usage

The [Command Palette](http://docs.sublimetext.info/en/latest/reference/command_palette.html) currently offers the following commands:

* Convert: CSON to JSON
* Convert: JSON to CSON
* Convert: Toggle Object Notation (CSON&#x27F7;JSON)

**Note:** Since automatic conversion is based on scope, make sure the a supported CoffeeScript package is installed as well. Using [Better CoffeeScript](https://packagecontrol.io/packages/Better%20CoffeeScript) is recommended, though [CoffeeScript](https://packagecontrol.io/packages/CoffeeScript), [IcedCoffeeScript](https://packagecontrol.io/packages/IcedCoffeeScript) and [Mongoose CoffeeScript](https://packagecontrol.io/packages/Mongoose%20CoffeeScript) are also supported.

### Keyboard Shortcuts

*The following examples all use the macOS shortcuts, for Linux or Windows use <kbd>Ctrl</kbd>+<kbd>Alt</kbd> rather than <kbd>Cmd</kbd>+<kbd>Alt</kbd>.*

Memorizing the keyboard shortcuts for conversion is easy. Just think of <kbd>C</kbd> for CSON and <kbd>J</kbd> for JSON:

* CSON to JSON (or C to J): <kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>C</kbd>, <kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>J</kbd>
* JSON to CSON (or J to C): <kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>J</kbd>, <kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>C</kbd>

### Settings

Some of the default conversion settings can be modified from the *Package Settings* menu:

* Indentation level (`int`)
* Sort keys (`boolean`)

# License

This work is licensed under the [The MIT License](LICENSE).

## Donate

You are welcome support this project using [Flattr](https://flattr.com/submit/auto?user_id=idleberg&url=https://github.com/idleberg/sublime-cson-converter) or Bitcoin `17CXJuPsmhuTzFV2k4RKYwpEHVjskJktRd`
