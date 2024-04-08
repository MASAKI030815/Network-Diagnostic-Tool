import time
import tkinter as tk
import tkinter.font as tkFont
from display_gateway_v4 import display_gateway_v4
from display_myip_v4 import display_myip_v4
from view_all import view_all


if __name__ == '__main__':
    view_all()
    while True:
        display_gateway_v4()
        display_myip_v4()
        time.sleep(1)