import netifaces
import ping_gateway_v4
import tkinter as tk
import tkinter.font as tkFont
from ping_gateway_v4 import ping_gateway_v4

def display_gateway_v4():
    title = "-------Gateway Ping Results-------\n"
    results = ping_gateway_v4()
    short_result = results['short']
    large_result = results['large']

    # 全体のステータスがOKかNGかを判断し、NGのみを表示
    if short_result != 0 or large_result != 0:
        overall_status_text = "NG"
    else:
        overall_status_text = "OK"

    gateway_ip = netifaces.gateways()['default'][netifaces.AF_INET][0]
    result_text = f"{title}{overall_status_text} (Short / Large) : {gateway_ip}\n\n"

    return result_text,overall_status_text,short_result,large_result

