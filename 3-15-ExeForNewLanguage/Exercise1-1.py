import time
import curses

def main(stdscr):
    i = 0

    while stdscr.getch() != 27: # Code for ESC key

        print(str(i) + " " + str(c))
        time.sleep(0.5)
        i+=1
        
        #if c == 27:
        #    break   # Exit the while loop for ES
        #elif c == ord('q'):
        #    break   # Exit the while loop

curses.wrapper(main)
