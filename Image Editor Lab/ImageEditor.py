from graphics import*
from Button import*

def brighten(cats):
    for x in range (430):
        for y in range (497):
            pixel = cats.getPixel(x,y)
            r = pixel[0] + 46
            g = pixel[1] + 46
            b = pixel[2] + 46
            if r + 46 > 255:
                r = 255
            if g + 46 > 255:
                g = 255
            if b + 46 > 255:
                b = 255
            cats.setPixel(x,y,color_rgb(r,g,b))            

def darken(cats):
    for x in range (430):
        for y in range (497):
            pixel = cats.getPixel(x,y)
            r = pixel[0] - 46
            g = pixel[1] - 46
            b = pixel[2] - 46
            if r - 46 < 0:
                r = 0
            if g - 46 < 0:
                g = 0
            if b - 46 < 0:
                b = 0
            cats.setPixel(x,y,color_rgb(r,g,b))

def blurr(cats):               

    
    return None

def contrast(cats):

    for x in range (430):
        for y in range (497):
 
            pixel = cats.getPixel(x,y)

            if pixel[0] < 128:
            
                r = pixel[0] - 46
                g = pixel[1] - 46
                b = pixel[2] - 46
                if r - 46 < 0:
                    r = 0
                if g - 46 < 0:
                    g = 0
                if b - 46 < 0:
                    b = 0
                cats.setPixel(x,y,color_rgb(r,g,b))

            else:
                    pixel = cats.getPixel(x,y)
                    r = pixel[0] + 46
                    g = pixel[1] + 46
                    b = pixel[2] + 46
                    if r + 46 > 255:
                        r = 255
                    if g + 46 > 255:
                        g = 255
                    if b + 46 > 255:
                        b = 255
                    cats.setPixel(x,y,color_rgb(r,g,b)) 

    
def specialFilter(cats):
    for x in range (430):
        for y in range (497):
            pixel = cats.getPixel(x,y)
            r = pixel[0] + 46
            g = 0
            b = pixel[0] + 46
            if r + 76 > 255:
                r = 255
            if g + 6 > 255:
                g = 255
            if b + 70 > 255:
                b = 255
            cats.setPixel(x,y,color_rgb(r,g,b))            


def main():

    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "mediumaquamarine", "Show", Point(70, 40), 45)
    hi = Button(win, "mediumaquamarine", "Hide", Point(180, 40), 45)
    close = Button(win, "grey", "Quit", Point(110, 560), 45)
    bright = Button(win, "gold", "Brighten", Point(720, 50), 45)
    dark = Button(win, "gold", "Darken", Point(720, 150), 45)
    blur = Button(win, "gold", "Blur", Point(720, 250), 45)
    cont = Button(win, "gold", "Contrast", Point(720, 350), 45)
    filt = Button(win, "gold", "Filter", Point(720, 450), 45)

    cats = Image(Point(450,300), "Cats.png")

    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            cats.undraw()
            cats.draw(win)
        if hi.isClicked(m):
            cats.undraw()
        if dark.isClicked(m):
            darken(cats)
        if bright.isClicked(m):
            brighten(cats)
        if blur.isClicked(m):
            blurr(cats)
        if cont.isClicked(m):
            contrast(cats)
        if filt.isClicked(m):
            specialFilter(cats)
        m = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()
