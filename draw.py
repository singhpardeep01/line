from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    A = y1 - y0
    B = x0 - x1
    if ( B > 0 ):
        #3456
        if ( A > 0 ):
            #34
        else:
            #56
    else:
        #1278
        if ( A > 0 ):
            #12
            if ( A < -1*B ):
                #1
                octant1( x0, y0, x1, y1, screen, color )
            else:
                #2
                octant2( x0, y0, x1, y1, screen, color )
        else:
            #78
            if ( -1*A < -1*B ):
                #8
                octant8( x0, y0, x1, y1, screen, color )
            else:
                #7
                octant7( x0, y0, x1, y1, screen, color )


def octant1( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1
    d = 2*A + B
    while x <= x1:
        plot( screen, color, x, y )
        if ( d > 0 ):
            y += 1
            d += 2*B
        x += 1
        d += 2*A
    pass
def octant2( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1
    d = A + 2*B
    while y <= y1:
        plot( screen, color, x, y )
        if ( d < 0 ):
            x += 1
            d += 2*A
        y += 1
        d += 2*B
    pass
def octant7( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1
    d = A - 2*B
    while y >= y1:
        plot( screen, color, x, y )
        if ( d > 0 ):
            x += 1
            d += 2*A
        y -= 1
        d -= 2*B
    pass    
def octant8( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1
    d = 2*A - B
    while x <= x1:
        plot( screen, color, x, y )
        if ( d < 0 ):
            y -= 1
            d -= 2*B
        x += 1
        d += 2*A
    pass
