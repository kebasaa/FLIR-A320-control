# FLIR-A320-control
This program is based on Python 3 on Windows and can be used to control a [FLIR A320 infrared camera](http://flir.com/uploadedFiles/Security/Products/A-Series/a3xxPT-Series-Users-Manual.pdf) through telnet. It shouldn't be difficult to port to other systems. The main functions include some settings and a logging functionality that takes a picture at regular intervals.

## Requirements: Install modules

In the command window, enter:

    pip3 install PyQt5

## To convert .ui (Qt Designer file) to .py

In the command window, enter:

    pyuic5 -o Interface.py Interface.ui

## License

### Software

This software is distributed under the GPL version 3.

### Logos and icons

All logos and icons are trademark of [FLIR](https://www.flir.com/).


