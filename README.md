Code is meant to be used with an Arduino Uno on https://www.adafruit.com/product/420

Code is tested on python 3.5.2 with just pillow library installed. (pip3 install pillow)

The code itself should be pretty good about giving useful errors. If someone misnames their images, they should get something informative like: “FileNotFoundError: [Errno 2] No such file or directory: '1.bmp'”

Images must be named exactly, “1.bmp” “2.bmp” and “3.bmp” and bmp must be lower case or you will get a file not found error. The code can of course be adapted to use any filenames and has been set up to play nice with many image types out of the box (Thanks pillow!)

The command to run is “python3 images_to_arduino.py” and the images have to be put in the folder with the script BEFORE running this command.

The script will convert the images to full Arduino code, ready to upload (As long as the Arduino IDEs have the library for the panels installed already.) Arduino code will show up in a folder called LED_Panel_Arduino_Code, which will appear in the same folder as the script.

Arduino code has been tested to run on 1.6.13. You'll need the Adafruit libraries they give you. If you can run their example code on your LED panel, then the generated code should work.


```
Code is released under the following license:

Copyright (c) 2017 Orlando Science Center

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
