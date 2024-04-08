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