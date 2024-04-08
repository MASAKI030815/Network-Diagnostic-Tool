import myip_local_v4v6
import tkinter as tk
import tkinter.font as tkFont
from myip_local_v4v6 import myip_local_v4v6

def display_myip_v4():
    ipv6_addr = ipv4_addr = netmask = gateway = interface = None
    results = {interface,ipv4_addr,netmask,gateway,ipv6_addr}
    title = "-------Network Setting-------\n"
    results_text = f"{title}"
    results = myip_local_v4v6()

    if results[0]:
        results_text += f"Interface: {results[0]}\n"

    if results[1] and results[2]:
        results_text += f"IPv4 Address: {results[1]}\n"
        results_text += f"Netmask: {results[2]}\n"

    if results[3]:
        results_text += f"Default Gateway: {results[3]}\n"

    if results[4]:
        results_text += f"IPv6 Address: {results[4]}\n"

    return results_text
