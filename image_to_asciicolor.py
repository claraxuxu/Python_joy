from PIL import Image  # use the Pillow library, for download : sudo pip install Pillow
from math import *
import os

IMG= 'pics/cat.jpg'  

path = os.path.join(os.getcwd(), IMG)
img = Image.open(path)

WIDTH= int (round(img.size[0] / 5))   #get current image's width
HEIGHT=int (round(img.size[1] / 10)) # get current image's height and reduce its height as the interspace between each line is wider than the one between each character

ascii_char = list(" .'`^\",:;Il!i><~+_-?][}{1)(\|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")  

def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    length = len(ascii_char)
    gray = int(0.213 * r + 0.72 * g + 0.072 * b) # give a standard to grey part
    unit = (256.0 + 1) / length
    #return ascii_char[int(gray / unit)] # characters
    color = 16 + (floor(5 / 256 * r) * 36) + (floor(5 / 256 * g) * 6) + floor(5 / 256 * b)
    return "\33[48;5;" + str(color) + "m" + " " + "\33[0m"

if __name__=='__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(get_char(*im.getpixel((j, i)))),
        print('') 

    print (txt)
    with open("result/output-color.txt", 'w') as f:  #write the result in this file
        f.write(txt)