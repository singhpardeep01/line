from random import *
from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
'''
draw_line( 250, 250, 499, 300, screen, color ) #1
draw_line( 250, 250, 300, 499, screen, color ) #2
draw_line( 250, 250, 300, 0, screen, color )   #7
draw_line( 250, 250, 499, 200, screen, color ) #8
draw_line( 250, 250, 200, 499, screen, color ) #3
draw_line( 250, 250, 0, 300, screen, color ) #4
draw_line( 250, 250, 0, 200, screen, color )   #5
draw_line( 250, 250, 200, 0, screen, color ) #6
draw_line( 0, 250, 499, 250, screen, color ) #horizontal
draw_line( 250, 0, 250, 499, screen, color ) #vertical
draw_line( 0, 0, 499, 499, screen, color ) #m=1
draw_line( 0, 499, 499, 0, screen, color ) #m=-1
'''
'''
#random lines
x = 0
while ( x < 100000000 ):
    color = [ randint( 0, 255 ), randint( 0, 255 ),
              randint( 0, 255 ) ]
    draw_line( randint( 0, 499 ), randint( 0, 499 ),
               randint( 0, 499 ), randint( 0, 499 ),
               screen, color )
    x += 1
'''
draw_line( 0, 0, 499, 499, screen, color )
draw_line( 0, 499, 499, 0, screen, color )
draw_line( 0, 250, 499, 250, screen, color )
draw_line( 250, 0, 250, 499, screen, color )
draw_line( 0, 0, 0, 499, screen, color )
draw_line( 0, 0, 499, 0, screen, color )
draw_line( 499, 0, 499, 499, screen, color )
draw_line( 0, 499, 499, 499, screen, color )
draw_line( 0, 0, 250, 499, screen, color )
draw_line( 0, 0, 499, 250, screen, color )
draw_line( 0, 499, 250, 0, screen, color )
draw_line( 0, 499, 499, 250, screen, color )
draw_line( 499, 0, 0, 250, screen, color )
draw_line( 499, 0, 250, 499, screen, color )
draw_line( 499, 499, 0, 250, screen, color )
draw_line( 499, 499, 250, 0, screen, color )
draw_line( 250, 0, 0, 250, screen, color )
draw_line( 0, 250, 250, 499, screen, color )
draw_line( 250, 499, 499, 250, screen, color )
draw_line( 499, 250, 250, 0, screen, color )


display(screen)
save_extension(screen, 'img.png')
