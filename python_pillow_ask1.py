from PIL import Image, ImageChops


def clap(im):
    blg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, blg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    box = diff.getbbox()
    if box:
        return im.crop(box)


im = Image.open("image.png")
im = clap(im)
im.save('res.png')
