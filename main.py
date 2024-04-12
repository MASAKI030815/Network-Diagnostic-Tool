import tkinter as tk
import tkinter.font as tkFont
import threading
from get_myip import display_myip_v4
from command_internet_pingv6 import display_gateway_v4

class App:
    def __init__(self, root):
        self.root = root
        # 各関数の実行状態を追跡するためのロック
        self.myip_lock = threading.Lock()
        self.gateway_lock = threading.Lock()

        self.root.title("Network Diagnostic Tool")
        self.root.configure(bg="black")
        self.widget_myip_text = tk.Text(root, height=7, width=60, bg="black", fg="white", borderwidth=0, highlightthickness=0)
        self.widget_myip_text.grid(row=0, column=0, padx=10, pady=10)
        self.widget_gateway_text = tk.Text(root, height=3, width=60, bg="black", fg="white", borderwidth=0, highlightthickness=0)
        self.widget_gateway_text.grid(row=1, column=0, padx=10, pady=10)
        self.update_gui()

    def fetch_myip(self):
        if not self.myip_lock.acquire(blocking=False):
            # すでに別のスレッドがこの関数を実行中の場合は戻る
            return
        try:
            results_myip = display_myip_v4()
            # メインスレッドでのGUI更新のためにスケジュール
            self.root.after(0, self.update_myip, results_myip)
        finally:
            # 実行が完了したらロックを解放
            self.myip_lock.release()

    def update_myip(self, results_myip):
        # GUIを更新...
        bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        self.widget_myip_text.delete("1.0", tk.END)
        self.widget_myip_text.insert(tk.END, results_myip)
        self.widget_myip_text.tag_add("1", "1.0", "1.end")
        self.widget_myip_text.tag_config("1", foreground="yellow", font=bold_font)

    def fetch_gateway(self):
        if not self.gateway_lock.acquire(blocking=False):
            # すでに別のスレッドがこの関数を実行中の場合は戻る
            return
        try:
            results_gateway = display_gateway_v4()
            # メインスレッドでのGUI更新のためにスケジュール
            self.root.after(0, self.update_gateway, results_gateway)
        finally:
            # 実行が完了したらロックを解放
            self.gateway_lock.release()

    def update_gateway(self, results_gateway):
        # GUIを更新...
        bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        self.widget_gateway_text.delete("1.0", tk.END)
        self.widget_gateway_text.insert(tk.END, results_gateway[0])
        self.widget_gateway_text.tag_add("title", "1.0", "1.end")
        self.widget_gateway_text.tag_config("title", foreground="yellow", font=bold_font)    
        # 全体のステータスに対するタグ設定
        self.widget_gateway_text.tag_add("overall", "2.0", f"2.{len(results_gateway[1])}")
        self.widget_gateway_text.tag_config("overall", foreground="green" if results_gateway[1] == "OK" else "red", font=bold_font)
        # Short の結果に適用するタグを追加（文字色で表示）
        self.widget_gateway_text.tag_add("short", "2.4", "2.10")  # "Short"
        self.widget_gateway_text.tag_config("short", foreground="green" if results_gateway[2] == 0 else "red", font=bold_font)
        # Large の結果に適用するタグを追加（文字色で表示）
        self.widget_gateway_text.tag_add("large", "2.12", "2.17")  # "Large"
        self.widget_gateway_text.tag_config("large", foreground="green" if results_gateway[3] == 0 else "red", font=bold_font)

    def update_gui(self):
        myip_thread = threading.Thread(target=self.fetch_myip)
        #myip_thread.setDaemon(True)  # スレッドをデーモンスレッドとして設定
        myip_thread.start()
        gateway_thread = threading.Thread(target=self.fetch_gateway)
        #gateway_thread.setDaemon(True)  # スレッドをデーモンスレッドとして設定
        gateway_thread.start()

        self.root.after(100, self.update_gui)

root = tk.Tk()
app = App(root)
root.mainloop()
