from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
#draw_line( 0, 0, 500, 249, screen, color )
draw_line( 250, 250, 500, 300, screen, color ) #1
draw_line( 250, 250, 300, 500, screen, color ) #2
draw_line( 250, 250, 300, 0, screen, color )   #7
draw_line( 250, 250, 500, 200, screen, color ) #8
draw_line( 250, 250, 200, 500, screen, color ) #3
draw_line( 250, 250, 0, 300, screen, color ) #4
draw_line( 250, 250, 0, 200, screen, color )   #5
draw_line( 250, 250, 200, 0, screen, color ) #6

display(screen)
save_extension(screen, 'img.png')
