import curses

def main(stdscr):

    while True:

        c = stdscr.getch()
        if c == 27: # ESC code
            break   # Exit the while loop for ESC

curses.wrapper(main)
