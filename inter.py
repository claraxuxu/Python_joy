import os
from PIL import Image, ImageFont, ImageDraw
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o','--output')

ascii_char = list("MNHQ$OC67)oa+>!:+. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__=='__main__':
    im = Image.open("pics/cat.jpg")
    WIDTH = int(im.width/6)
    HEIGHT = int(im.height/15)
    im_txt = Image.new("RGB",(im.width,im.height),(255,255,255))
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ""
    colors = []
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pixel = im.getpixel((j,i))
            colors.append((pixel[0],pixel[1],pixel[2]))
            if(len(pixel) == 4):
                txt += get_char(pixel[0],pixel[1],pixel[2],pixel[3])
            else:
                txt += get_char(pixel[0],pixel[1],pixel[2])        
        txt += '\n' 
        colors.append((255,255,255))
    dr = ImageDraw.Draw(im_txt)
    font=ImageFont.load_default().font
    x=y=0
    font_w,font_h=font.getsize(txt[1])
    font_h *= 1.5
    for i in range(len(txt)):
        if(txt[i]=='\n'):
            x+=font_h
            y=-font_w
        dr.text([y,x],txt[i],colors[i])
        y+=font_w
    im_txt.save("result/inter-pic.png")