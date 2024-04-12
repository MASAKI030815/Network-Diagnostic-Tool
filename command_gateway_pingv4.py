import subprocess
import netifaces
import config


def Gateway_pingv4():
    gateway = interface = None
    name = "Default Gateway"

    try:
        default_gateway = netifaces.gateways().get('default', {}).get(netifaces.AF_INET)
        if default_gateway:
            interface = default_gateway[1]
            addrs = netifaces.ifaddresses(interface)
            gateway = default_gateway[0]
            if netifaces.AF_INET6 in addrs:
                for addr_info in addrs[netifaces.AF_INET6]:
                    if not addr_info['addr'].startswith('fe80'):
                        break
    except Exception as e:
        print(f"IPアドレス取得中にエラーが発生しました: {e}")

    return gateway,name

def pingv4(ipv4,name):
    results = {}
    short_packet_cmd = ["ping"] + config.pingv4_short_option + [ipv4]
    short_packet_result = subprocess.run(short_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['short'] = short_packet_result.returncode

    large_packet_cmd = ["ping"] + config.pingv4_large_option + [ipv4]
    large_packet_result = subprocess.run(large_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['large'] = large_packet_result.returncode

    short_result = results['short']
    large_result = results['large']
    #print(ipv4,name,short_result,large_result)
    return ipv4,name,short_result,large_result