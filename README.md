Code is meant to be used with an Arduino Uno on https://www.adafruit.com/product/420

Code is tested on python 3.5.2 with just pillow library installed. (pip3 install pillow)

The code itself should be pretty good about giving useful errors. If someone misnames their images, they should get something informative like: “FileNotFoundError: [Errno 2] No such file or directory: '1.bmp'”

Images must be named exactly, “1.bmp” “2.bmp” and “3.bmp” and bmp must be lower case or you will get a file not found error. The code can of course be adapted to use any filenames and has been set up to play nice with many image types out of the box (Thanks pillow!)

The command to run is “python3 images_to_arduino.py” and the images have to be put in the folder with the script BEFORE running this command.

The script will convert the images to full Arduino code, ready to upload (As long as the Arduino IDEs have the library for the panels installed already.) Arduino code will show up in a folder called LED_Panel_Arduino_Code, which will appear in the same folder as the script.

Arduino code has been tested to run on 1.6.13. You'll need the Adafruit libraries they give you. If you can run their example code on your LED panel, then the generated code should work.