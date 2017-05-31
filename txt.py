import getch
from curtsies import Input

# def detect():
#     while True:
#         x = ord(getch.getch())
#         if x == 65:
#             print("U")
#         elif x == 66:
#             print("D")
#         elif x == 67:
#             print("L")
#         elif x == 68:
#             print("R")


def detect():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            print(repr(e))


try:
    detect()
except KeyboardInterrupt:
    print("close")
