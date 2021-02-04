
from PIL import Image  # use the Pillow library, for download : sudo pip install Pillow
import os

IMG= 'pics/cat.jpg'  


path = os.path.join(os.getcwd(), IMG)
img = Image.open(path)

WIDTH = int(round(img.size[0] /10)) #get current image's width
HEIGHT = int (round(img.size[1] / 18)) # get current image's height and reduce its height as the interspace between each line is wider than the one between each character

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")  

def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.21 * r + 0.72 * g + 0.07 * b) # give a standard to grey part
    unit = (256.0 + 1) / length
    
    return ascii_char[int(gray / unit)] # different degree of grey has their different character from the ascii_char list

if __name__=='__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n' 

    print (txt)
    with open("result/output.txt", 'w') as f:  #write the result in this file
        f.write(txt)