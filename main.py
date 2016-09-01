from PIL import Image, ImageDraw, ImageFont


def gen_img(img_size=(32, 32), bg_color=(255, 255, 255, 0), fillcolor=(0, 0, 0), line1='', line2='', line3='', mode='RGBA'):
    """Generate an image with up to 3 line of text.
    Font: https://managore.itch.io/m5x7
    """
    img = Image.new(mode, img_size, bg_color)
    fnt = ImageFont.truetype('m5x7.ttf', 16)
    d = ImageDraw.Draw(img)
    line1 and d.text((1, -3), line1, font=fnt, fill=fillcolor)
    line2 and d.text((1, 7), line2, font=fnt, fill=fillcolor)
    line3 and d.text((1, 17), line3, font=fnt, fill=fillcolor)
    del d
    return img
