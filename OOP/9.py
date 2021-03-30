import os, glob
from PIL import Image, ImageDraw, ImageColor, ImageFont

def convert_image(ext, new_ext):
    for infile in glob.glob('*' + ext):
        file, extension = os.path.splitext(infile)
        fill_color = (255, 255, 255)
        text = 'Hello,\nWorld!'
        size = 300
        im = Image.open(infile)
        fontpath="tahoma.ttf"
        tahoma = ImageFont.truetype(fontpath, 78)
        # Убираем маску непрозрачности на png. Можно было просто сменить режим на RGB,
        # но мне показалось что дополнительно залить фон белым будет правильнее.
        # Вот ссылка на issue библиотеки https://github.com/python-pillow/Pillow/issues/2609
        if im.mode in ('RGBA', 'LA'):
            background = Image.new(im.mode[:-1],  im.size, fill_color)
            background.paste(im, im.split()[-1])
            im = background
            draw =  ImageDraw.Draw(im)
            img_width, img_height = im.size
            draw.rectangle([(img_width - size) / 2, (img_height - size) / 2, (img_width + size) / 2, (img_height + size) / 2], width=10)
            draw.multiline_text([(img_width - size) / 2, (img_height - size) / 2, (img_width + size) / 2, (img_height + size) / 2], text, fill=(0,0,0), font=tahoma)
        im.save(file + new_ext, 'JPEG')
        del draw
    if im:
        return 1
    else:
        return 0

ext = '.png'
new_ext = '.jpg'
con_img = convert_image(ext, new_ext)
"""
def draw_image(new_ext):
    for infile in glob.glob('*' + new_ext):
        im = Image.open(infile)
        draw = ImageDraw.Draw(im)
        draw.


for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    draw = ImageDraw.Draw(im)
    draw.multiline_text((200, 200), 'I love \n YOU!')
    im.save(file + '.thumbnail', 'JPEG')
    del draw
"""