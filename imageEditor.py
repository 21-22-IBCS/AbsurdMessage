'''ex photo (500x451)
 loop through every pix and change value by 20'''

def darken (cats):
    for i in range (500) #500px in width
        for j in range (451) #451 px tall
            pix = cats.getPixel(i,j) #
            r, g, b = pix[0]-20, pix[1] -20, pix[2] -20
            if r -20 < 0:
                r = 0
            if g -20 < 0:
                g = 0
            if b -20 < 0:
                b = 0


       ''' getPixel (x,y)
            returns a list [R,G,B]

        setPixel (x,y, color)
            color_rbg(r,g,b) creates a color based on 3 values
