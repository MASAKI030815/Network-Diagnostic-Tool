import subprocess
import threading
import config

def Internet_pingv4(ipv4,name):
    results = {}
    short_packet_cmd = ["ping"] + config.pingv4_short_option + [ipv4[0]]
    short_packet_result = subprocess.run(short_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['short'] = short_packet_result.returncode

    large_packet_cmd = ["ping"] + config.pingv4_large_option + [ipv4[0]]
    large_packet_result = subprocess.run(large_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['large'] = large_packet_result.returncode

    short_result = results['short']
    large_result = results['large']
    #print(ipv4,name,short_result,large_result)
    return ipv4,name,short_result,large_result

# 各IPアドレスに対してスレッドを作成してpingを実行
threads_Internet_pingv4 = []
for target in config.pingv4_targets:
    ipv4,name = target
    thread = threading.Thread(target=Internet_pingv4, args=(ipv4,name))
    thread.start()
    threads_Internet_pingv4.append(thread)

# すべてのスレッドが終了するのを待つ
for thread in threads_Internet_pingv4:
    thread.join()
