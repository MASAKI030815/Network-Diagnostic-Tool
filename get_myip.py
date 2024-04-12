import netifaces

def myip_v4v6():
    ipv6_addr = ipv4_addr = netmask = gateway = interface = None

    try:
        # デフォルトの IPv4 ゲートウェイが存在するか確認
        default_gateway = netifaces.gateways().get('default', {}).get(netifaces.AF_INET)

        if default_gateway:
            interface = default_gateway[1]
            addrs = netifaces.ifaddresses(interface)

            if netifaces.AF_INET in addrs:
                ipv4_info = addrs[netifaces.AF_INET][0]
                ipv4_addr = ipv4_info.get('addr')
                netmask = ipv4_info.get('netmask')
            
            gateway = default_gateway[0]

            if netifaces.AF_INET6 in addrs:
                for addr_info in addrs[netifaces.AF_INET6]:
                    if not addr_info['addr'].startswith('fe80'):
                        ipv6_addr = addr_info['addr'].split('%')[0]
                        break

    except Exception as e:
        print(f"IPアドレス取得中にエラーが発生しました: {e}")
    #print(interface,ipv4_addr,netmask,gateway,ipv6_addr)
    return interface,ipv4_addr,netmask,gateway,ipv6_addr



