import tkinter as tk
import tkinter.font as tkFont
from display_gateway_v4 import display_gateway_v4
from display_myip_v4 import display_myip_v4

def view_all():
    root = tk.Tk()
    root.title("Network Diagnostic Tool")
    root.configure(bg="black")
    results_myip = display_myip_v4()
    results_gateway = display_gateway_v4()

    widget_myip_text = tk.Text(root, height=7, width=60, bg="black", fg="white",borderwidth=0, highlightthickness=0)
    widget_myip_text.grid(row=0, column=0, padx=10, pady=10)

    widget_gateway_text = tk.Text(root, height=3, width=60, bg="black", fg="white",borderwidth=0, highlightthickness=0)
    widget_gateway_text.grid(row=1, column=0, padx=10, pady=10)

    bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
    widget_myip_text.insert(tk.END, results_myip)
    widget_myip_text.tag_add(f"1", f"1.0",f"1.end")
    widget_myip_text.tag_config(f"1", foreground="yellow",font=bold_font)

    bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
    widget_gateway_text.insert(tk.END,results_gateway[0])
    widget_gateway_text.tag_add(f"1", f"1.0",f"1.end")
    widget_gateway_text.tag_config(f"1", foreground="yellow",font=bold_font)    
    # 全体のステータスに対するタグ設定
    widget_gateway_text.tag_add("overall", "2.0", f"2.{len(results_gateway[1])}")
    widget_gateway_text.tag_config("overall", foreground="green" if results_gateway[1] == "OK" else "red", font=bold_font)
    # Short の結果に適用するタグを追加（文字色で表示）
    widget_gateway_text.tag_add("short", "2.4", "2.10")  # "Short"
    widget_gateway_text.tag_config("short", foreground="green" if results_gateway[2] == 0 else "red", font=bold_font)
    # Large の結果に適用するタグを追加（文字色で表示）
    widget_gateway_text.tag_add("large", "2.12", "2.17")  # "Large"
    widget_gateway_text.tag_config("large", foreground="green" if results_gateway[3] == 0 else "red", font=bold_font)

    root.mainloop()