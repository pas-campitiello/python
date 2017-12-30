import _thread, time, sys

def input_thread(L):
    input()
    print("aaaaa")    
    #L.append(None)
    
def do_print():
    L = []
    _thread.start_new_thread(input_thread, (L,))
    i = 0    
    while 1:
        time.sleep(1)
        if L: break
        print(i)
        i += 1
       
do_print()

