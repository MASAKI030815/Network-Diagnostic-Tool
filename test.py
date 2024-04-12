
from get_myip import myip_v4v6
import threading
from command_gateway_pingv4 import Gateway_pingv4
from command_internet_pingv4 import Internet_pingv4
from command_internet_pingv6 import Internet_pingv6
import config

ipv4,namev4 = config.pingv4_targets
ipv6,namev6 = config.pingv6_targets

# スレッドを作成して関数を実行
thread1 = threading.Thread(target=myip_v4v6)
thread2 = threading.Thread(target=Gateway_pingv4)
thread3 = threading.Thread(target=Internet_pingv4, args=(ipv4,namev4))
thread4 = threading.Thread(target=Internet_pingv6, args=(ipv6,namev6))

# スレッドを開始
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# すべてのスレッドが終了するのを待つ
thread1.join()
thread2.join()
thread3.join()
thread4.join()


