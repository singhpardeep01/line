from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
draw_line( screen, 0, 499, 300, 400, color )
display(screen)
save_extension(screen, 'img.png')
