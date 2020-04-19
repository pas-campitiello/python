import curses
import time

def main(win):

    win.nodelay(1)
    init = 0
    prec = 0    
    next = 1

    while win.getch() != 27:
        win.addstr("{0}\n".format(str(next)))
           
        prec = next     
        next = next + init
        init = prec
        
        time.sleep(0.5)

curses.wrapper(main)


