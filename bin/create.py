from pngcanvas import PNGCanvas
from math import ceil

white = (0xff,0xff,0xff,0xff)
blue = (0,0x30,0xbf,0xdf)
red = (0xff,0,0,0xff)
green = (0,0xff,0,0xff)
gray = (0x7f,0x7f,0x7f,0xff)
clear = (0xff,0xff,0xff,0x00)

# there's a quirk with the png canvas lib, we can't start out with a
# transparent background, so we go with white, then create a transparent bg
# as a once over when creating the images
line_color = gray
bg_color = white
transparent_bg = True


colors_eq = lambda c1,c2: all(x==y for x,y in zip(c1,c2))

def mk_transparent(img, target_color):
    """
    accepts a png canvas image object and converts the given color into
    transparent pixels
    """
    for x in range(img.width):
        for y in range(img.height):
            o = img._offset(x, y)
            if colors_eq(img.canvas[o:o+4], target_color):
                for i in range(4):
                    img.canvas[o+i] = clear[i]
    return img


def normalize_vals(vals, w, h, minv=None, maxv=None):
    if maxv is None:
        mn,mx = min(vals), max(vals)
    else:
        mn,mx = minv,maxv
    vv = []
    for i,v in enumerate(vals):
        drawval = h - int(((v - mn)/mx) * h) if mx else 1
        if drawval == 0: drawval = 1
        if drawval == h: drawval -= 1
        vv.append(drawval)
    return vv


def mkbar(vals, w, h,
        minv=None, maxv=None,
        clr=green,
        bgclr=white,
        transparent_bg=True):
    png = PNGCanvas(w,h,color=clr, bgcolor=bgclr)
    vv = normalize_vals(vals, w, h, minv, maxv)
    stepw = ceil(w / (len(vv)))
    for i,y in enumerate(vv):
        png.filled_rectangle((stepw * i)+2, h, stepw*(i+1)-4, y)
    if transparent_bg: png = mk_transparent(png, bgclr)
    return png.dump()


# take a list of lists and flatten it out
def flatten(lst):
    def fl_(ls):
        for sublist in ls:
            for mem in sublist:
                yield mem
    return list(fl_(lst))


def mkline(vals, w, h,
        minv=None, maxv=None,
        clr=green, bgclr=white,
        transparent_bg=True ):
    if len(vals) < w/2:
        vals = flatten(zip(vals,vals))
    mn,mx = minv,maxv
    vv = []
    for i,v in enumerate(vals):
        drawval = h - int(((v - mn)/mx) * h *.8) if mx else 1
        if drawval == 0: drawval = .9*h
        if drawval == h: drawval -= .1*h
        vv.append(drawval)

    png = PNGCanvas(w,h,color=clr, bgcolor=bgclr)
    dv = [ (vv[i],vv[i+1]) for i in range(len(vv)-1)]
    stepw = ceil(w / (len(dv)))
    for i,(y0,y1) in enumerate(dv):
        for pad in range(-7,8):
            png.line((stepw * i), y0+pad, stepw*(i+1), y1+pad)
    if transparent_bg: png = mk_transparent(png, bgclr)
    return png.dump()


if __name__ == '__main__':



    w,h=128,128

    for b in [0,1,2]:
        for c in [0,1,2]:
            for d in [0,1,2]:
                for e in [0,1,2]:
                    for f in [0,1,2]:
                        # make all the 3 value chartmoji
                        n = f"out/bar/chart_bar{b}{c}{d}{e}{f}.png"
                        print(n)
                        with open(n, 'wb') as of:
                            of.write(
                                mkbar(
                                    [b,c,d,e,f], w, h, 0, 2,
                                    clr=line_color, bgclr=bg_color,
                                    transparent_bg=transparent_bg ) )
                        n = f"out/line/chart_ln{b}{c}{d}{e}{f}.png"
                        print(n)
                        with open(n, 'wb') as of:
                            of.write(
                                mkline(
                                    [b,c,d,e,f], w, h, 0, 2,
                                    clr=line_color, bgclr=bg_color,
                                    transparent_bg=transparent_bg ) )

