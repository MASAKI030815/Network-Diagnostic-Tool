import netifaces
import subprocess
import config

def ping_gateway_v4():
    results = {}
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    
    short_packet_cmd = ["ping"] + config.pingv4_short_option + [default_gateway]
    short_packet_result = subprocess.run(short_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['short'] = short_packet_result.returncode

    large_packet_cmd = ["ping"] + config.pingv4_large_option + [default_gateway]
    large_packet_result = subprocess.run(large_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['large'] = large_packet_result.returncode
    return results

def display_gateway_v4():
    title = "-------Gateway Ping Results-------\n"
    results = ping_gateway_v4()
    short_result = results['short']
    large_result = results['large']

    # 全体のステータスがOKかNGかを判断し、NGのみを表示
    if short_result == 0 and large_result == 0:
        overall_status_text = "OK"
    else:
        overall_status_text = "NG"

    gateway_ip = netifaces.gateways()['default'][netifaces.AF_INET][0]
    result_text = f"{title}{overall_status_text} (Short / Large) : {gateway_ip}\n\n"

    return result_text,overall_status_text,short_result,large_result






#ping_gateway_v4()
