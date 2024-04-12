import subprocess
import threading
import config

def Internet_pingv6(ipv6,name):
    results = {}
    short_packet_cmd = ["ping"] + config.pingv6_short_option + [ipv6[0]]
    short_packet_result = subprocess.run(short_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['short'] = short_packet_result.returncode

    large_packet_cmd = ["ping"] + config.pingv6_large_option + [ipv6[0]]
    large_packet_result = subprocess.run(large_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['large'] = large_packet_result.returncode

    short_result = results['short']
    large_result = results['large']
    #print(ipv6,name,short_result,large_result)
    return ipv6,name,short_result,large_result

# 各IPアドレスに対してスレッドを作成してpingを実行
threads_Internet_pingv6 = []
for target in config.pingv6_targets:
    ipv6,name = target
    thread = threading.Thread(target=Internet_pingv6, args=(ipv6,name))
    thread.start()
    threads_Internet_pingv6.append(thread)

# すべてのスレッドが終了するのを待つ
for thread in threads_Internet_pingv6:
    thread.join()
