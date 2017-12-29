import winsound

print("Hi Barb, what note to play?")

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
run = 1

while(run):
    inp = getch()

    note = 2500

    if inp == b'c' :
        note = 1046
    elif inp == b'd':
        note = 1174
    elif inp == b'e':
        note = 1318
    elif inp == b'f':
        note = 1396
    elif inp == b'g':
        note = 1567	
    elif inp == b'a':
        note = 1760	
    elif inp == b'b':
        note = 1975
    elif inp == b'q':
        run = 0
        print("Bye")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    else:
        print("Invalid input, try again. Choose from c d e f g a b. q to quit")

    if run != 0:    
        winsound.Beep(note, 100)
