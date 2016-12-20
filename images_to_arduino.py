from PIL import Image                 # This is our image processing library
import os                             # For folder creation and checking

delay = 1000
divideby = 36.46 # The higher this number is, the dimmer the display will be and the fewer colors it will be displaying. It should be 36.42 

im1 = Image.open("1.bmp")
im2 = Image.open("2.bmp")
im3 = Image.open("3.bmp")

rgb_im1 = im1.convert("RGB")          # This converts the images to an RGB image, this is necessary for some formats, such as GIF.
rgb_im2 = im2.convert("RGB")          
rgb_im3 = im3.convert("RGB")         

ardu_image1r = "const PROGMEM byte image1_rmap[512] = {"
ardu_image1g = "const PROGMEM byte image1_gmap[512] = {"
ardu_image1b = "const PROGMEM byte image1_bmap[512] = {"

ardu_image2r = "const PROGMEM byte image2_rmap[512] = {"
ardu_image2g = "const PROGMEM byte image2_gmap[512] = {"
ardu_image2b = "const PROGMEM byte image2_bmap[512] = {"

ardu_image3r = "const PROGMEM byte image3_rmap[512] = {"
ardu_image3g = "const PROGMEM byte image3_gmap[512] = {"
ardu_image3b = "const PROGMEM byte image3_bmap[512] = {"

# Image 1
for y in range(0, 16):                          # These for loops read every pixel in the image and write the arduino code lines that are that image
    for x in range(0, 32):
        r, g, b = rgb_im1.getpixel((x, y))
        
        r = str(int(round(r / divideby)))       # These are because the arduino code needs colors ranging from 0 to 7.
        g = str(int(round(g / divideby)))
        b = str(int(round(b / divideby)))

        # This actually writes the arduino code for this particular image
        #ardu_image1 += "  matrix.drawPixel(" + str(x) + ", " + str(y) + ", matrix.Color333(" + r + ", " + g + ", " + b + "));\n"
        ardu_image1r += r + ", "
        ardu_image1g += g + ", "
        ardu_image1b += b + ", "
        
ardu_image1r += "};\n"
ardu_image1g += "};\n"
ardu_image1b += "};\n\n"

# Image 2
for y in range(0, 16):                          # These for loops read every pixel in the image and write the arduino code lines that are that image
    for x in range(0, 32):
        r, g, b = rgb_im2.getpixel((x, y))
        
        r = str(int(round(r / divideby)))       # These are because the arduino code needs colors ranging from 0 to 7.
        g = str(int(round(g / divideby)))
        b = str(int(round(b / divideby)))

        # This actually writes the arduino code for this particular image
        #ardu_image1 += "  matrix.drawPixel(" + str(x) + ", " + str(y) + ", matrix.Color333(" + r + ", " + g + ", " + b + "));\n"
        ardu_image2r += r + ", "
        ardu_image2g += g + ", "
        ardu_image2b += b + ", "
        
ardu_image2r += "};\n"
ardu_image2g += "};\n"
ardu_image2b += "};\n\n"

# Image 1
for y in range(0, 16):                          # These for loops read every pixel in the image and write the arduino code lines that are that image
    for x in range(0, 32):
        r, g, b = rgb_im3.getpixel((x, y))
        
        r = str(int(round(r / divideby)))       # These are because the arduino code needs colors ranging from 0 to 7.
        g = str(int(round(g / divideby)))
        b = str(int(round(b / divideby)))

        # This actually writes the arduino code for this particular image
        #ardu_image1 += "  matrix.drawPixel(" + str(x) + ", " + str(y) + ", matrix.Color333(" + r + ", " + g + ", " + b + "));\n"
        ardu_image3r += r + ", "
        ardu_image3g += g + ", "
        ardu_image3b += b + ", "
        
ardu_image3r += "};\n"
ardu_image3g += "};\n"
ardu_image3b += "};\n\n"

# You can change delaytime to change how fast the pictures progress

code_header = """#include <Adafruit_GFX.h>   // Core graphics library
#include <RGBmatrixPanel.h> // Hardware-specific library
#include <avr/pgmspace.h>

#define CLK 8  // MUST be on PORTB!
#define LAT A3
#define OE  9
#define A   A0
#define B   A1
#define C   A2
RGBmatrixPanel matrix(A, B, C, CLK, LAT, OE, false);

int delayTime = 1000;
int i = 0;

void setup() {
  matrix.begin();
}

"""

image_init_area = ardu_image1r + ardu_image1g + ardu_image1b + ardu_image2r + ardu_image2g + ardu_image2b + ardu_image3r + ardu_image3g + ardu_image3b

code_footer = """
void loop() {
  i = 0;

  for (int y = 0; y < 16; y++){
    for (int x = 0; x < 32; x++){
      matrix.drawPixel(x, y, matrix.Color333(pgm_read_byte_near(image1_rmap + i), pgm_read_byte_near(image1_gmap + i), pgm_read_byte_near(image1_bmap + i)));
      i++;
    }  
  }

  delay(delayTime);
  
  i = 0;

  for (int y = 0; y < 16; y++){
    for (int x = 0; x < 32; x++){
      matrix.drawPixel(x, y, matrix.Color333(pgm_read_byte_near(image2_rmap + i), pgm_read_byte_near(image2_gmap + i), pgm_read_byte_near(image2_bmap + i)));
      i++;
    }  
  }

  delay(delayTime);
  
  i = 0;

  for (int y = 0; y < 16; y++){
    for (int x = 0; x < 32; x++){
      matrix.drawPixel(x, y, matrix.Color333(pgm_read_byte_near(image3_rmap + i), pgm_read_byte_near(image3_gmap + i), pgm_read_byte_near(image3_bmap + i)));
      i++;
    }  
  }

  delay(delayTime);
}
"""

code_full = code_header + image_init_area + code_footer # code_delay + ardu_image2 + code_delay + ardu_image3 + code_footer

if not os.path.exists("LED_Panel_Arduino_Code"):
    os.makedirs("LED_Panel_Arduino_Code")

with open("LED_Panel_Arduino_Code\LED_Panel_Arduino_Code.ino", "w") as arduino_output_file:
    print(code_full, file=arduino_output_file)

print ("File Written")