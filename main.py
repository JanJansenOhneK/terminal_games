
from time import sleep
from sys import stdout
import sys
from colorama import Style,Fore

menu_index = 0
menu_id = "start"

MENU_IDTOINDEX = [
    "start",
    "main"
]

frame_index = 0


def set_menu(id:str) -> None:
    global menu_index
    try:
        menu_index = MENU_IDTOINDEX.index(id)
    except ValueError:
        print(f"{Fore.RED}set_menu: Menu id not found{Style.RESET_ALL}")
        raise ValueError

def frame() -> str:
    if menu_id == "start":
        set_menu("main")
        return f"""
Be Patient, it is starting.
"""
    elif menu_id == "main":
        return f"""
Terminal Games by JanJansenOhneK
"""


stdout.write("\n\n\n")
stdout.flush()
while True:
    menu_id = MENU_IDTOINDEX[menu_index]
    stdout.write(f"\r{frame().strip()}")
    stdout.flush()
    frame_index += 1
    