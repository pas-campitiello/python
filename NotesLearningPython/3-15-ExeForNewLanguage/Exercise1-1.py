import curses
import time

def main(win):

    win.nodelay(1)
    i = 0

    while win.getch() != 27:
        win.addstr("{0}\n".format(str(i)))
        i+=1
        time.sleep(0.1)

curses.wrapper(main)

