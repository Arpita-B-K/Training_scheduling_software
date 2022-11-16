
from CLI import *
#from GUI import *

def input_choice():
    cli_types = ["CLI", "Cli", "cli", "cLi", "clI", "CLi", "ClI", "cLI"]
    gui_types = ["GUI", "Gui", "gui", "gUi", "guI", "GUi", "GuI", "gUI"]
    flag = 1
    while flag:
        choice = input("do you want to input through CLI or GUI ?:")
        print("\n")
        if choice in gui_types:
            flag = 0
            # input_through_gui()
        elif choice in cli_types:
            flag = 0
            
        else:
            print("invalid Input  !! ")

